from django.db import models
from clases.models import Clase

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    correo = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100, null=True)

    clases = models.ManyToManyField(Clase, related_name='estudiantes')

    def __str__(self):
        return self.nombre
