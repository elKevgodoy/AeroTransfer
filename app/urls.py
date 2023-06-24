from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro', views.registro, name='registro'),
    path('reserva', views.reserva, name='reserva'),
    path('listaTransfers/', views.listaTransfers, name='listaTransfers'),
    path('historial_viajes', views.historial_viajes, name='historial_viajes'),
    path('perfil', views.perfil, name='perfil'),
    path('loginConductor', views.loginConductor, name='loginConductor'),
    path('perfilConductor', views.perfilConductor, name='perfilConductor'),
    path('reservaTransfer/', views.ReservaTransfer, name='reservaTransfer'),
    path('login/', views.login_view, name='login'),
    path('reservasActuales/', views.reservas_actuales, name='ReservasActuales'),
]