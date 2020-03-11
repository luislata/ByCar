from django.db import models
# Create your models here.

class Persona(models.Model):
    nombre_completo = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField()