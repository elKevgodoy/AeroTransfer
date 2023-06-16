from django.db import models

# Create your models here.
class Totem(models.Model):
    id_totem = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)

class Transfer(models.Model):
    id_transfer = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    asientos_disponibles = models.IntegerField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()

class HistorialViajes(models.Model):
    id_Historial = models.AutoField(primary_key=True)
    fecha= models.DateField()
    destino= models.CharField(max_length= 100)
    pasajeros= models.IntegerField()