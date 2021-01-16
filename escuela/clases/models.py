from django.db import models


class Clase(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    creditos = models.IntegerField()
    descripcion = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre
