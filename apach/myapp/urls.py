"""Es mejor que cada aplicación tenga las urls de sus vistas
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.About),
    path('Veterinarios/', views.Veterinary),
    path('Tareas/', views.Task),
    path('Donar/', views.donar),
    path('signup/', views.Registrarse),
    path('logout/', views.cerrar_secion, name="logout"),
    path('signin/', views.signin, name="signin"),
    path('Noticias/', views.News),

]