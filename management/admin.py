from django.contrib import admin
from .models import Parking, ParkingSpace, Ticket, SubscriptionPlan, Subscriber, Car

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('nome', 'location', 'hour_price')

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('cod', 'status', 'parking')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa', 'hora_entrada', 'hora_saida', 'vaga', 'valor')

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_plan')
    
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'modelo', 'placa')
