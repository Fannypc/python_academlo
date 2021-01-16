from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from autores.models import Autor
from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = (AllowAny,)

    # esta funcion es para filtrar los resultados
    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item in ['page_size']:
                continue
            if item in ['editorial', 'autores']:
                # para buscar las relaciones de libros por id (tiene relacion con
                # editorial y con autores
                query[item + '__id'] = self.request.query_params[item]
                # asi seria si queremos buscar por nombre
                #query[item + '__nombre'] = self.request.query_params[item]
                continue
            query[item + '__contains'] = self.request.query_params[item]

        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

    @action(methods=['GET', 'POST'], detail=True)
    def autores(self, request, pk=None):
        libro = self.get_object()
        if request.method == 'GET':
            serialized = AutorSerializer(libro.autores, many=True)
            return Response(status=status.HTTP_200_OK,data=serialized.data)
        if request.method == 'POST':
            autores_id = request.data['autores_ids']
            for autor_id in autores_id:
                autor = Autor.objects.get(id=autor_id)
                libro.autores.add(autor)

            return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True, url_path='editorial_get')
    def editorial(self, request, pk=None):
        libro = self.get_object()
        serialized = EditorialSerializer(libro.editorial)
        return Response(status=status.HTTP_200_OK,data=serialized.data)

    @action(methods=['POST'], detail=True)
    def name_change(self, request, pk=None):
        libro = self.get_object()

        data = request.data
        libro.nombre = data['name']
        libro.save()

        return Response(status=status.HTTP_200_OK)
