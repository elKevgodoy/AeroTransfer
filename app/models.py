from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    asientosdisponibles= models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoauto = models.CharField(max_length=30, verbose_name="Tipo")
    Disponible = models.BooleanField()

    def __str__(self):
        return self.patente

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    destino = models.CharField(max_length=120, verbose_name="Destino")
    nombre= models.CharField(max_length=20, verbose_name="Nombre")
    apellido= models.CharField(max_length=20, verbose_name="Apellido")
    telefono= models.IntegerField()
    conductor= models.ForeignKey(Conductor, on_delete=models.CASCADE)
    asientos = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo= models.EmailField()
    fecha_reserva = models.CharField(max_length=50)

    def __int__(self):
        return self.id_reserva
