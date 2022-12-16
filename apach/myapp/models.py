from django.db import models

# Create your models here.
class veterinarios(models.Model):
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + " " + self.apellido

class tareas(models.Model):
    descripcion = models.CharField(max_length=75)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=75)
    responsable = models.ForeignKey(veterinarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion + " - " + self.lugar + " - " + str(self.fecha) + " - " + self.responsable.nombre + " - " + self.responsable.apellido