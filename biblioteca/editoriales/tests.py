from django.test import TestCase
from rest_framework.test import APITestCase

from autores.models import Autor
from editoriales.models import Editorial


class FiltrarEditorialTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000'
        self.editorial = Editorial.objects.create(

        )
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

    def test_filter_editoriales(self):
        query = f'nombre={self.autor.nombre}'

        response = self.client.get(
            f'{self.url}/editoriales/?{query}'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(
            response.data['results'][0]['nombre'],
            self.autor.nombre
        )
