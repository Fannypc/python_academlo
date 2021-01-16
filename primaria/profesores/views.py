from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profesores.models import Profesor
from profesores.serializers import ProfesorSerializer


class ProfesorList(APIView):
    def get(self, request):
        profesores = Profesor.objects.all()
        serialized = ProfesorSerializer(profesores, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def post(self, request):
        serialized = ProfesorSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=serialized.errors)


class ProfesorDetail(APIView):
    def get_object(self, profesor_id):
        try:
            return Profesor.objects.get(id=profesor_id)
        except Profesor.DoesNotExist:
            raise Http404

    def get(self, request, profesor_id):
        profesor_obj = self.get_object(profesor_id)
        serialized = ProfesorSerializer(instance=profesor_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def put(self, request, profesor_id):
        profesor_obj = self.get_object(profesor_id)
        serialized = ProfesorSerializer(instance=profesor_obj,
                                          data=request.data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)

    def delete(self, request, profesor_id):
        profesor_obj = get_object_or_404(Profesor, id=profesor_id)
        profesor_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

