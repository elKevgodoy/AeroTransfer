from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Conductor, Reserva
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request): 
    return render(request, 'home.html')



def login_view(request):
    datos = {}
    if request.method == 'POST':
        try:
            username = request.POST['usuario']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                datos['usuario'] = username
                datos['password'] = password
                datos['error'] = 'Usuario o contraseña incorrectos'
                return render(request, 'login.html', datos)
        
        except KeyError:
            return render(request, 'registration/login.html', {'error': 'Datos del formulario incompletos'})
    else:
        return render(request, 'registration/login.html')
    



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
            datos['error'] = 'Lo sentimos, al parecer el conductor ya tiene sus asientos ocupados. Intentalo nuevamente Error 1 '
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
                                       asientos=asientos, correo=correo, fecha_reserva=fecha, estado=True)
                cantasientos=conductor.asientosdisponibles
                conductor.asientosdisponibles=int(cantasientos)-int(asientos)
                conductor.save()
                mensaje="¡El conductor se pondrá en contacto contigo dentro de poco! ID Reserva:"+str(id)
                messages.success(request, mensaje)
                return redirect(to="home")
            except: 
                datos['error'] = 'Lo sentimos, al parecer el conductor ya tiene sus asientos ocupados. Intentalo nuevamente Error 2' 
                return render(request, 'Registro_Reserva.html',datos)  

    except:
        datos['existe']=0
        datos['error'] = 'Parecer ser que ha ocurrido un error, intentelo nuevamente. error 3 '
        return render(request, 'Registro_Reserva.html',datos)
    



def historial_viajes(request): 
    return render(request, 'historial_viajes.html')

def perfil(request): 
    return render(request, 'perfil.html')

def loginConductor(request):
    return render(request, 'loginConductor.html')



@login_required(login_url='/accounts/login/')
def perfilConductor(request):
    datos={} 
    datos['persona']=conductor=Conductor.objects.get(username=request.user)
    if request.method=='POST':
        if 'disponibilidad' in request.POST:
            conductor.Disponible=True
            conductor.save()
            datos['mensaje']="Disponibilidad cambiada correctamente"
            return render(request, 'perfilConductor.html', datos)
        else:
            conductor.Disponible=False
            conductor.save()
            datos['mensaje']="Disponibilidad cambiada correctamente"
            return render(request, 'perfilConductor.html', datos)
    else:
        return render(request, 'perfilConductor.html', datos)
    




@login_required(login_url='/accounts/login/')
def reservas_actuales(request):
    try:
        datos={}
        conductor=Conductor.objects.get(username=request.user)
        datos['reserva']=Reserva.objects.filter(conductor=conductor, estado=True)
        datos['existe']=1
        return render(request, 'Reservas_Actuales.html',datos)

    except:
        datos['existe']=0
        return render(request, 'Reservas_Actuales.html',datos)



    