from rest_framework import serializers

from editoriales.models import Editorial


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'
