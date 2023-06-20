from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Totem(models.Model):
    id_totem = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.id_totem

class Transfer(models.Model):
    id_transfer = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    asientos_disponibles = models.IntegerField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id_transfer

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.id_usuario

class Conductor(models.Model):
    licencia = models.CharField(max_length=9)
    patente = models.CharField(max_length=6, primary_key=True, verbose_name="Patente")
    asientos = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()

    def __str__(self):
        return self.id_reserva

class HistorialViajes(models.Model):
    id_Historial = models.AutoField(primary_key=True)
    fecha= models.DateField()
    destino= models.CharField(max_length= 100)
    pasajeros= models.IntegerField()

    def __str__(self):
        return self.id_Historial

