from django.test import TestCase
from rest_framework.test import APITestCase

from autores.models import Autor
from editoriales.models import Editorial
from libros.models import Libro


class FiltrarAutorTestCase(APITestCase):
    def setUp(self):
        self.url='http://127.0.0.1:8000'
        self.autor = Autor.objects.create(
            nombre='John',
            telefono='4425156',
            correo='jonh@gmail.com',
            edad=20
        )
        self.autor = Autor.objects.create(
            nombre='Mary',
            telefono='4425156',
            correo='jonh@gmail.com',
            edad=20
        )

    def test_filter_autores(self):
        query = f'nombre={self.autor.nombre}'

        response = self.client.get(
            f'{self.url}/autores/?{query}'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(
            response.data['results'][0]['nombre'],
            self.autor.nombre
        )

class AutoresActionTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000'
        self.editorial = Editorial.objects.create(
            nombre='Editorial 10',
            direccion="Enrigue",
            telefono='4516'
        )
        self.autor = Autor.objects.create(
            nombre='Mary',
            telefono='4425156',
            correo='jonh@gmail.com',
            edad=20
        )
        for _ in range(3):
            self.libro = Libro.objects.create(
                nombre='libro 10',
                fecha_publicacion='2020-12-10',
                paginas=30,
                editorial=self.editorial
            )
            self.autor.libros.add(self.libro)

    def test_get_libros_action(self):
        print(self.libro.id)
        response = self.client.get(
            f'{self.url}/autores/{self.autor.id}/libros/',
        )
        #self.libro.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
