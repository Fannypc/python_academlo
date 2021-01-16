from django.db import models

from profesores.models import Profesor


class Materia(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    creditos = models.IntegerField()
    descripcion = models.CharField(max_length=50, null=True)

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre