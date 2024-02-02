from rest_framework import serializers, response, status
from core.models import *

#UD10.2

class ModuloListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = (
            'id',
            '__str__',
        )

class ModuloDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = (
            '__all__'
        )

class RAListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResAprendizaje
        fields = (
            'id',
            '__str__',
        )

class RADetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResAprendizaje
        fields = (
            '__all__'
        )
class CEListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CritEvaluacion
        fields = (
            'id',
            'minimo',
            '__str__',
        )

class CEDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CritEvaluacion
        fields = (
            '__all__'
        )
