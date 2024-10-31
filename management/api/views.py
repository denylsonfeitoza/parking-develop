from rest_framework import generics
from .models import Parking, ParkingSpace, Ticket
from .serializers import ParkingSerializer, ParkingSpaceSerializer, TicketSerializer

# Listar e criar estacionamentos
class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

# Detalhes, atualização e exclusão de um estacionamento específico
class ParkingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

# Listar e criar vagas
class ParkingSpaceList(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer

# Detalhes, atualização e exclusão de uma vaga específica
class ParkingSpaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer

# Adicione views para os Tickets se necessário
class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
