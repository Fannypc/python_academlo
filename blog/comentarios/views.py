from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from publicaciones.serializers import PublicacionSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination

    @action(methods=['GET'], detail=True)
    def publicacion(self, request, pk=None):
        comentario = self.get_object()
        serialized = PublicacionSerializer(comentario.publicacion)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
