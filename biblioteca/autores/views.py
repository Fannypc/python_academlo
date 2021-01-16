from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from autores.models import Autor
from autores.serializers import AutorSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (AllowAny,)

    # esta funcion es para filtrar los resultados
    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item in ['page_size']:
                continue
            query[item + '__contains'] = self.request.query_params[item]

        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

    @action(methods=['GET','POST'], detail=True)
    def libros(self, request, pk=None):
        autor = self.get_object()
        if request.method == 'GET':
            serialized = LibroSerializer(autor.libros, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST':
            libros_id = request.data['libros_ids']
            for libro_id in libros_id:
                libro = Libro.objects.get(id=libro_id)
                autor.libros.add(libro)

            return Response(status=status.HTTP_200_OK)
