from django.shortcuts import render

def home(request): 
    return render(request, 'home.html')

def registro(request): 
    return render(request, 'registro.html')

def reserva(request): 
    return render(request, 'reserva.html')