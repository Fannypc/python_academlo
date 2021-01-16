from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    #pagination_class = PageNumberPagination

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicaciones(self, request, pk=None):
        tag = self.get_object()
        if request.method == 'GET':
            serialized = PublicacionSerializer(tag.publicaciones, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method in ['POST', 'DELETE']:
            publicaciones_id = request.data['publicaciones_ids']
            code = status.HTTP_200_OK
            for publicacion_id in publicaciones_id:
                publicacion = get_object_or_404(id=publicacion_id)
                if request.method == 'POST':
                    tag.publicaciones.add(publicacion)
                    code = status.HTTP_201_CREATED
                else:
                    tag.publicaciones.remove(publicacion)
                    code = status.HTTP_204_NO_CONTENT
            return Response(status=code)

