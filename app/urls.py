from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro', views.registro, name='registro'),
    path('reserva', views.reserva, name='reserva')
]