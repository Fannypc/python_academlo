from django.db import models


# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
