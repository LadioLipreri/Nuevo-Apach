from django.contrib import admin
from .models import veterinarios, tareas, Categoria, Noticia
# Register your models here.

admin.site.register(veterinarios)

admin.site.register(tareas)

admin.site.register(Categoria)

admin.site.register(Noticia)