from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import veterinarios, tareas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
def index(request):
    return render(request, 'index.html')


def donar(request):
    return render(request, 'donar.html')


def Hello(request):
    return HttpResponse("<h1>Hello word</h1>")


def About(request):
    return HttpResponse("<h1>About</h1>")


def Registrarse(request):
    if request.method == 'GET':  # Cuando se envia el formulario
        return render(request, "signup.html", {
            'form': UserCreationForm
        })
    else:  # Cuando recibe los datos
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
            })

def cerrar_secion(request):
    logout(request)
    return redirect('home')

def Veterinary(request):  # el nombre de la vista y del modelo no deben ser iguales
    # misveterinarios = list(veterinarios.objects.values())
    # return JsonResponse(misveterinarios, safe=False)
    misveterinarios = veterinarios.objects.all()
    return render(request, "veterinarios.html", {
        'misveterinarios': misveterinarios
    })


def Task(request):
    # mistareas = tareas.objects.get(id=id)
    mistareas = tareas.objects.all()
    # return HttpResponse('tarea: %s' % mistareas.descripcion)
    return render(request, "tareas.html", {
        'mistareas': mistareas
    })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password1'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos.'
            })
        else:
            login(request, user)
            return redirect('home')



    
    