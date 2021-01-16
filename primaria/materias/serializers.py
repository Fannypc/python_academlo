from rest_framework import serializers

from estudiantes.serializers import EstudianteSerializer
from materias.models import Materia

"""class MateriaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
"""


class MateriaSerializer(serializers.ModelSerializer):
    #estudiantes = EstudianteSerializer(read_only=True)
    estudiantes = serializers.SerializerMethodField()

    class Meta:
        model = Materia
        fields = '__all__'

    # para obtener los estudiantes relacionados a la materia
    def get_estudiantes(self, obj):
        estudiantes=obj.estudiantes.all()
        response = EstudianteSerializer(estudiantes, many=True).data
        return response

