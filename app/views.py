from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Conductor, Reserva
from django.contrib.auth.models import User
from datetime import date

def home(request): 
    return render(request, 'home.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            patente=Conductor.objects.get(patente=request.POST['patente'])
            if(patente):
                data['nombre'] = request.POST['first_name']
                data['apellido'] = request.POST['last_name']
                data['usuario'] = request.POST['username']
                data['patente'] = request.POST['patente']
                data['licencia'] = request.POST['licencia']
                data['asientos'] = request.POST['asientos']
                data['vehiculo'] = request.POST['vehiculo']
                data['error']="Esa patente ya esta registrada en el sistema"
                return render(request, 'registration/registro.html', data)
            else:
                formulario.save()
                user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
                #login(request, user)
                usuario=User.objects.get(username=formulario.cleaned_data["username"])
                Conductor.objects.create(licencia=request.POST['licencia'], patente=request.POST['patente'], asientos=request.POST['asientos'], tipoauto=request.POST['vehiculo'], Disponible=True, username=usuario)
                messages.success(request, "Te has registrado correctamente")
                return redirect(to="home")
        else:
            data['nombre'] = request.POST['first_name']
            data['apellido'] = request.POST['last_name']
            data['usuario'] = request.POST['username']
            data['patente'] = request.POST['patente']
            data['licencia'] = request.POST['licencia']
            data['asientos'] = request.POST['asientos']
            data['vehiculo'] = request.POST['vehiculo']
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
        
        calle=request.POST['inputCalle']
        numero=request.POST['inputNumero']
        ciudad=request.POST['inputCiudad']
        datos['destino']=ciudad+', '+calle+' '+numero
        datos['asientos']=asientosrequeridos=request.POST['inputPasajeros']
        persona=Conductor.objects.filter(asientosdisponibles__gte=asientosrequeridos, Disponible=True)
        datos['personas']=persona
        datos['existe']=1
        return render(request, 'listaTransfers.html',datos)
    except:
        datos['existe']=0
        datos['error'] = 'Parecer ser que ha ocurrido un error, intentelo nuevamente.'
        return render(request, 'listaTransfers.html',datos)
    
    
def ReservaTransfer(request):
    datos={
        
    }
    try:
        datos['username']=usuario=request.POST['username']
        datos['destino']=destino=request.POST['destino']
        datos['asientos']=asientos=request.POST['asientos']
        usuario=User.objects.get(username=usuario) 
        conductor=Conductor.objects.get(username=usuario)

        datos['persona']=conductor
        if int(asientos) > int(conductor.asientosdisponibles): #Esto en el caso de que al último momento otro pasajero reserve con dicho conductor
            datos['existe']=0
            datos['error'] = 'Lo sentimos, al parecer el conductor ya tiene sus asientos ocupados. Intentalo nuevamente error 1'
            return render(request, 'Registro_Reserva.html',datos)
        else: #En caso de que si existan asientos disponibles en base a los asientos requeridos
            datos['existe']=1

            try: #Esto es para confirmar si ya envio otro formulario con los datos de nombre, apellido, correo y numero ya ingresados
                nombre=request.POST['first_name']
                apellido=request.POST['last_name']
                correo=request.POST['email']
                numero=request.POST['telefono']
                id=int(Reserva.objects.count())
                id=id+1
                fecha=str(date.today())
                Reserva.objects.create(id_reserva=id, destino=destino, nombre=nombre, apellido=apellido, telefono=numero, conductor=conductor, \
                                       asientos=asientos, correo=correo, fecha_reserva=fecha)
                return redirect(to="home")
            except: 
                datos['error'] = 'Lo sentimos, al parecer el conductor ya tiene sus asientos ocupados. Intentalo nuevamente error 3' 
                return render(request, 'Registro_Reserva.html',datos)  

    except:
        datos['existe']=0
        datos['error'] = 'Parecer ser que ha ocurrido un error, intentelo nuevamente. error 2 '
        return render(request, 'Registro_Reserva.html',datos)
    



def historial_viajes(request): 
    return render(request, 'historial_viajes.html')

def perfil(request): 
    return render(request, 'perfil.html')

def loginConductor(request):
    return render(request, 'loginConductor.html')

def perfilConductor(request):
    return render(request, 'perfilConductor.html')