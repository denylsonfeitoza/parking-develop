from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Parking, ParkingSpace, Ticket, SubscriptionPlan, Subscriber, Car
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token


class ParkingManagementTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='1testpass')
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')


class ParkingTests(ParkingManagementTestCase):
    def test_create_parking(self):
        data = {
            "nome": "Estacionamento Central",
            "location": "Rua Principal, 123",
            "hour_price": 5.0
        }
        response = self.client.post(reverse('parking-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_parking_spaces(self):
        parking = Parking.objects.create(nome="Estacionamento Central", location="Rua Principal, 123", hour_price=5.0)
        ParkingSpace.objects.create(cod="A1", status=False, parking=parking)
        response = self.client.get(reverse('parking-space-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ParkingSpaceTests(ParkingManagementTestCase):
    def test_list_pcd_parking_spaces(self):
        parking = Parking.objects.create(nome="Estacionamento Central", location="Rua Principal, 123", hour_price=5.0)
        ParkingSpace.objects.create(cod="P1", status=False, parking=parking, is_pcd=True)
        response = self.client.get(reverse('pcd-parking-space-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TicketTests(ParkingManagementTestCase):
    def test_calculate_ticket_value(self):
        parking = Parking.objects.create(nome="Estacionamento Central", location="Rua Principal, 123", hour_price=5.0)
        parking_space = ParkingSpace.objects.create(cod="A1", status=False, parking=parking)
        ticket = Ticket.objects.create(modelo="Modelo X", placa="ABC1234", hora_entrada=timezone.now(), vaga=parking_space)
        ticket.hora_saida = timezone.now() + timezone.timedelta(hours=2)
        ticket.calcular_valor()
        response = self.client.get(reverse('ticket-detail', args=[ticket.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ticket.valor, 10.0)


class SubscriptionPlanTests(ParkingManagementTestCase):
    def test_list_subscription_plans(self):
        SubscriptionPlan.objects.create(name="Plano Mensal", price=50.0, duration=30)
        response = self.client.get(reverse('subscription-plan-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriberTests(ParkingManagementTestCase):
    def test_list_subscribers(self):
        plan = SubscriptionPlan.objects.create(name="Plano Mensal", price=50.0, duration=30)
        Subscriber.objects.create(user=self.user, subscription_plan=plan)
        response = self.client.get(reverse('subscriber-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CarTests(ParkingManagementTestCase):
    def test_create_and_list_cars(self):
        plan = SubscriptionPlan.objects.create(name="Plano Mensal", price=50.0, duration=30)
        subscriber = Subscriber.objects.create(user=self.user, subscription_plan=plan)
        data = {
            "subscriber": subscriber.id,
            "modelo": "Modelo Y",
            "placa": "XYZ9876",
            "cor": "Vermelho"
        }
        response = self.client.post(reverse('car-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        list_response = self.client.get(reverse('car-list-create'))
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
