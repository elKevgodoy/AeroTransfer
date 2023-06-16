from django.shortcuts import render

def home(request): 
    return render(request, 'home.html')

def registro(request): 
    return render(request, 'registro.html')

def reserva(request): 
    return render(request, 'reserva.html')

def listaTransfers(request): 
    return render(request, 'listaTransfers.html')

def historial_viajes(request): 
    return render(request, 'historial_viajes.html')

def perfil(request): 
    return render(request, 'perfil.html')

def loginConductor(request):
    return render(request, 'loginConductor.html')

def perfilConductor(request):
    return render(request, 'perfilConductor.html')