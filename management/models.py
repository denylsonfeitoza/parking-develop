from django.db import models
from django.conf import settings
from django.utils import timezone

class Parking(models.Model):
    nome = models.CharField(max_length=100, default="Estacionamento Padrão")
    location = models.CharField(max_length=255, default="Local Padrão")
    hour_price = models.FloatField()

    def __str__(self):
        return f"{self.nome} - R${self.hour_price}/hora"

class ParkingSpace(models.Model):
    cod = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="spaces")
    is_pcd = models.BooleanField(default=False)

    def __str__(self):
        tipo_vaga = "PCD" if self.is_pcd else "Comum"
        status_vaga = "Ocupada" if self.status else "Livre"
        return f"Vaga {self.cod} - {tipo_vaga} - {status_vaga}"

class Ticket(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    hora_entrada = models.DateTimeField()
    hora_saida = models.DateTimeField(null=True, blank=True)
    vaga = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    valor = models.FloatField(null=True, blank=True)

    def calcular_valor(self):
        if self.hora_saida:
            duracao = self.hora_saida - self.hora_entrada
            horas = duracao.total_seconds() // 3600
            self.valor = horas * self.vaga.parking.hour_price
            self.save()

    def __str__(self):
        return f"Ticket {self.placa} - Vaga {self.vaga.cod}"

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_plan.name}"

class Car(models.Model):
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE, related_name="cars")
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=20, unique=True)
    cor = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"