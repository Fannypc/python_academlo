from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    permission_classes = (AllowAny,)

    # esta funcion es para filtrar los resultados
    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item in ['page_size']:
                continue
            query[item + '__contains'] = self.request.query_params[item]

        print(query)
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

    @action(methods=['GET'], detail=True)
    def libros(self, request, pk=None):
        editorial = self.get_object()
        libros = Libro.objects.filter(editorial_id=editorial.id)
        serialized = LibroSerializer(libros, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
