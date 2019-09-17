from rest_framework import serializers
from .models import Arduino 


class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arduino
        fields = (
            '__all__'
        )

