from django.db import models

from tags.models import Tag


class Publicacion(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    contenido = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='publicaciones')

    def __str__(self):
        return self.nombre
