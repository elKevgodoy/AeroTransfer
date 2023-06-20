from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Conductor
from django.contrib.auth.models import User

def home(request): 
    return render(request, 'home.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            usuario=User.objects.get(username=formulario.cleaned_data["username"])
            Conductor.objects.create(licencia=request.POST['licencia'], patente=request.POST['patente'], username=usuario)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        else:
            data['nombre'] = request.POST['first_name']
            data['apellido'] = request.POST['last_name']
            data['usuario'] = request.POST['username']
            data['patente'] = request.POST['patente']
            data['licencia'] = request.POST['licencia']
            data['error'] = 'Usuario o contraseña incorrectos'
            data['form'] = formulario
            return render(request, 'registration/registro.html', data)
    return render(request, 'registration/registro.html', data)




def reserva(request): 
    return render(request, 'reserva.html')

def listaTransfers(request): 
    datos={
        
    }
    try:
        asientosrequeridos=request.POST['inputPasajeros']
        persona=Conductor.objects.filter(asientos__gte=asientosrequeridos)
        datos['personas']=persona
        datos['existe']=1
        return render(request, 'listaTransfers.html',datos)
    except:
        datos['existe']=0
        datos['error'] = 'Parecer ser que ha ocurrido un error, intentelo nuevamente.'
        return render(request, 'listaTransfers.html',datos)
    
    

def historial_viajes(request): 
    return render(request, 'historial_viajes.html')

def perfil(request): 
    return render(request, 'perfil.html')

def loginConductor(request):
    return render(request, 'loginConductor.html')

def perfilConductor(request):
    return render(request, 'perfilConductor.html')