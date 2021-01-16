from django.db import models


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    telefono = models.IntegerField(null=True)
    correo = models.CharField(max_length=50, null=True)
    edad = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
