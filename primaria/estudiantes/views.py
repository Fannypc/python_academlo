from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializer


class EstudianteList(APIView):
    def get(self, request):
        estudiantes = Estudiante.objects.all()
        serialized = EstudianteSerializer(estudiantes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def post(self, request):
        serialized = EstudianteSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=serialized.errors)


class EstudianteDetail(APIView):
    def get_object(self, estudiante_id):
        try:
            return Estudiante.objects.get(id=estudiante_id)
        except Estudiante.DoesNotExist:
            raise Http404

    def get(self, request, estudiante_id):
        estudiante_obj = self.get_object(estudiante_id)
        serialized = EstudianteSerializer(instance=estudiante_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def put(self, request, estudiante_id):
        estudiante_obj = self.get_object(estudiante_id)
        serialized = EstudianteSerializer(instance=estudiante_obj,
                                          data=request.data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)

    def delete(self, request, estudiante_id):
        estudiante_obj = get_object_or_404(Estudiante, id=estudiante_id)
        estudiante_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

