from django.db import models

from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    correo = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre
