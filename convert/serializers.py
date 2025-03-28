from rest_framework import serializers
from .models import UnitConverter

class UnitConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitConverter
        fields = '__all__'