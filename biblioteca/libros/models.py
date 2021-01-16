from django.db import models

from autores.models import Autor
from editoriales.models import Editorial


class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()

    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    """related_name es el nombre con el que accedemos desde el modelo relacionado
    pero desde Libro se seguira pudiendo acceder con el nombre 'autores' a los autores"""
    autores = models.ManyToManyField(Autor, related_name='libros')

    """
    De la siguiente manera se declara la relacion muchos a muchos
    y con una nueva clase se define la nueva tabla por si queremos
    ponerle campos extra o editarla mas, y en la relacion se pone 
    el atributo through para definir la tabla intermedia
    autores = models.ManyToManyField(Autor, related_name='autores',
                                     through='LibroAutor')


class LibroAutor(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)
"""

    def __str__(self):
        return self.nombre
