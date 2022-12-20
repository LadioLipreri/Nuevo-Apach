from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import veterinarios, tareas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from django.urls import reverse_lazy
#from .models import Noticia, Categoria, Comentario
from django.contrib.auth.decorators import login_required

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
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos.'
            })
        else:
            login(request, user)
            return redirect('home')



'''Lo del profe'''
@login_required
def Listar_Noticias(request):
	contexto = {}

	id_categoria = request.GET.get('id',None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticia = id_categoria)
	else:
		n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS

	contexto['noticias'] = n

	cat = Categoria.objects.all().order_by('nombre')
	contexto['categorias'] = cat

	return render(request, 'noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

#{'nombre':'nicolas', 'apellido':'Tortosa', 'edad':33}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''


    
    