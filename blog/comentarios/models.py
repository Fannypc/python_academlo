from django.db import models

from publicaciones.models import Publicacion


class Comentario(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    contenido = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
