"""Es mejor que cada aplicación tenga las urls de sus vistas
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.About),
    path('Veterinarios/', views.Veterinary),
    path('Tareas/', views.Task),
    path('Donar/', views.donar),
]