from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class veterinarios(models.Model):
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + " " + self.apellido

class tareas(models.Model):
    titulo = models.CharField(max_length=75)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=75)
    responsable = models.ForeignKey(veterinarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - ' + self.descripcion + " - " + self.lugar + " - " + str(self.fecha) + " - " + self.responsable.nombre + " - " + self.responsable.apellido


#lo del profe
class Usuario(AbstractUser):
	pass

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

	titulo = models.CharField(max_length = 150)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'noticias')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{noticia}->{texto}"

