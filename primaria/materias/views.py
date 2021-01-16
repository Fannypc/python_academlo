from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from materias.models import Materia
from materias.serializers import MateriaSerializer


class MateriaList(APIView):
    def get(self, request):
        materias = Materia.objects.all()
        serialized = MateriaSerializer(materias, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def post(self, request):
        serialized = MateriaSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=serialized.errors)


class MateriaDetail(APIView):
    def get_object(self, materia_id):
        try:
            return Materia.objects.get(id=materia_id)
        except Materia.DoesNotExist:
            raise Http404

    def get(self, request, materia_id):
        materia_obj = self.get_object(materia_id)
        serialized = MateriaSerializer(instance=materia_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def put(self, request, materia_id):
        materia_obj = self.get_object(materia_id)
        serialized = MateriaSerializer(instance=materia_obj,
                                          data=request.data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)

    def delete(self, request, materia_id):
        materia_obj = get_object_or_404(Materia, id=materia_id)
        materia_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
