from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Parking, ParkingSpace, Ticket, SubscriptionPlan, Subscriber, Car
from .serializers import ParkingSerializer, ParkingSpaceSerializer, TicketSerializer, SubscriptionPlanSerializer, SubscriberSerializer, CarSerializer

class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = []

class ParkingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = []

class ParkingSpaceList(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = []

class ParkingSpaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = []

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.hora_saida:
            instance.calcular_valor()
        return instance

class SubscriptionPlanList(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = []

class SubscriptionPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = []

class SubscriberAvailableParkingsList(generics.ListAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        try:
            subscriber = Subscriber.objects.get(user=self.request.user)
        except Subscriber.DoesNotExist:
            return Parking.objects.none()
        return Parking.objects.all()

class SubscriberListCreateView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = []
    
class PCDParkingSpaceList(generics.ListAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = []

    def get_queryset(self):
        return ParkingSpace.objects.filter(is_pcd=True)

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = []

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = []