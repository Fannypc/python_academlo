from rest_framework import serializers

from autores.models import Autor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        #todos los campos
        #fields = '__all__'
        fields = ('nombre', 'telefono', 'correo')

