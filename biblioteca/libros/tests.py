from rest_framework.test import APITestCase

from autores.models import Autor
from editoriales.models import Editorial
from libros.models import Libro


class FiltrarLibroTestCase(APITestCase):
    def setUp(self):
        self.url='http://127.0.0.1:8000'
        self.autor = Autor.objects.create(
            nombre='John',
            telefono='4425156',
            correo='jonh@gmail.com',
            edad=20
        )
        self.editorial = Editorial.objects.create(
            nombre='Editorial 10',
            direccion="Enrigue",
            telefono='4516'
        )
        self.libro = Libro.objects.create(
            nombre='libro 10',
            fecha_publicacion='2020-12-10',
            paginas=30,
            editorial=self.editorial
        )
        self.libro.autores.add(self.autor)

        self.libro2 = Libro.objects.create(
            nombre='libro 12',
            fecha_publicacion='2020-12-10',
            paginas=30,
            editorial=self.editorial
        )
        self.libro2.autores.add(self.autor)

    def test_filter_libros(self):
        query = f'nombre={self.libro.nombre}'

        response = self.client.get(
            f'{self.url}/libros/?{query}'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(
            response.data['results'][0]['nombre'],
            self.libro.nombre
        )


class AutoresActionTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000'
        self.editorial = Editorial.objects.create(
            nombre='Editorial 10',
            direccion="Enrigue",
            telefono='4516'
        )
        self.libro = Libro.objects.create(
            nombre='libro 10',
            fecha_publicacion='2020-12-10',
            paginas=30,
            editorial=self.editorial
        )
        for _ in range(3):
            self.autor = Autor.objects.create(
                nombre='Jhon',
                telefono='5461654',
                correo='jhon@gmail.com',
                edad=20
            )
            self.libro.autores.add(self.autor)

    def test_get_autores_action(self):
        print(self.libro.id)
        response = self.client.get(
            f'{self.url}/libros/{self.libro.id}/autores/'
        )
        #self.libro.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
