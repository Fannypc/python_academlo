from django.db import models
from areas.models import Area
from managers.models import Manager


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    managers = models.ManyToManyField(Manager, related_name='empleados')

    def __str__(self):
        return self.nombre
