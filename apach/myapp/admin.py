from django.contrib import admin
from .models import veterinarios, tareas, Categorias, Noticias
# Register your models here.

admin.site.register(veterinarios)

admin.site.register(tareas)

admin.site.register(Categorias)

admin.site.register(Noticias)