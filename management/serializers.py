from rest_framework import serializers
from .models import Parking, ParkingSpace, Ticket, SubscriptionPlan, Subscriber, Car

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    valor_final = serializers.FloatField(read_only=True, source='valor')
    
    class Meta:
        model = Ticket
        fields = '__all__'
        
class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'