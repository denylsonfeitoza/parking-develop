from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Parking, ParkingSpace, Ticket, SubscriptionPlan, Subscriber, Car
from .serializers import ParkingSerializer, ParkingSpaceSerializer, TicketSerializer, SubscriptionPlanSerializer, SubscriberSerializer, CarSerializer

# Listar e criar estacionamentos
class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = []

# Detalhes, atualização e exclusão de um estacionamento específico
class ParkingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = []

# Listar e criar vagas
class ParkingSpaceList(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = []

# Detalhes, atualização e exclusão de uma vaga específica
class ParkingSpaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = []

# Listar e criar tickets
class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []

# Detalhes, atualização e exclusão de um ticket específico, com cálculo de valor
class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.hora_saida:
            instance.calcular_valor()
        return instance

# Listar e criar planos de assinatura
class SubscriptionPlanList(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = []

# Detalhes, atualização e exclusão de planos de assinatura
class SubscriptionPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = []

# Listar estacionamentos disponíveis para usuários assinantes
class SubscriberAvailableParkingsList(generics.ListAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        try:
            subscriber = Subscriber.objects.get(user=self.request.user)
        except Subscriber.DoesNotExist:
            return Parking.objects.none()
        return Parking.objects.all()

# View para listar e criar assinantes
class SubscriberListCreateView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = []
    
# Listar apenas as vagas PCD
class PCDParkingSpaceList(generics.ListAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = []

    def get_queryset(self):
        return ParkingSpace.objects.filter(is_pcd=True)
    
# Listar todos os carros de assinantes
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = []

# Detalhe, atualização e exclusão de um carro específico
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = []