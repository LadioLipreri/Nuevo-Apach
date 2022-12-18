from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import veterinarios, tareas
from django.contrib.auth.forms import UserCreationForm
def index(request):
    return render(request, 'index.html')

def donar(request):
    return render(request, 'donar.html')

def Hello(request):
    return HttpResponse("<h1>Hello word</h1>")

def About(request):
    return HttpResponse("<h1>About</h1>")

def Registrarse(request):
    return render(request, "signup.html",{
        'form':UserCreationForm
    })

def Veterinary(request):#el nombre de la vista y del modelo no deben ser iguales
    #misveterinarios = list(veterinarios.objects.values())
    #return JsonResponse(misveterinarios, safe=False)
    misveterinarios = veterinarios.objects.all()
    return render(request, "veterinarios.html",{
        'misveterinarios':misveterinarios
    })

def Task(request):
    #mistareas = tareas.objects.get(id=id)
    mistareas = tareas.objects.all()
    #return HttpResponse('tarea: %s' % mistareas.descripcion)
    return render(request, "tareas.html",{
        'mistareas':mistareas
    })