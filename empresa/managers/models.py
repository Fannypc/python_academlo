from django.db import models


class Manager(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
