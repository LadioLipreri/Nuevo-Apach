from django.db import models

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


class Categorias(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.title


class Noticias(models.Model):
    categoria=models.ForeignKey(Categorias, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title