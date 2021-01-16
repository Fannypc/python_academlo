from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from tags.models import Tag
from tags.serializers import TagSerializer


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination

    @action(methods=['GET'], detail=True)
    def comentarios(self, request, pk=None):
        publicacion = self.get_object()
        comentarios = Comentario.objects.filter(publicacion_id=publicacion.id)
        serialized = ComentarioSerializer(comentarios, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def tags(self, request, pk=None):
        publicacion = self.get_object()
        if request.method == 'GET':
            serialized = TagSerializer(publicacion.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method in ['POST', 'DELETE']:
            tags_id = request.data['tags_ids']
            code = status.HTTP_200_OK
            for tag_id in tags_id:
                tag = get_object_or_404(id=int(tag_id))
                if request.method == 'POST':
                    publicacion.tags.add(tag)
                    code = status.HTTP_201_CREATED
                else:
                    publicacion.tags.remove(tag)
                    code = status.HTTP_204_NO_CONTENT

            return Response(status=code)
