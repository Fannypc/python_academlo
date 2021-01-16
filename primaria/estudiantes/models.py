from django.db import models

from django.db import models

from materias.models import Materia


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    correo = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100, null=True)

    materias = models.ManyToManyField(Materia, related_name='estudiantes')

    def __str__(self):
        return self.nombre
