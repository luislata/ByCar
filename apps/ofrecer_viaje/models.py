from django.db import models
from apps.solicitar_viaje.models import Persona

# Create your models here.

class ofrecer_viaje(models.Model):
    nombre = models.CharField(max_length=50)
    telefono_contacto = models.CharField(max_length=20)
    lugar_de_partida = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.CharField(max_length=20)
    asientos_disponibles = models.IntegerField()
    costo = models.IntegerField()
    persona = models.ForeignKey(Persona, null= True, blank=True, on_delete=models.CASCADE)