from rest_framework import serializers, response, status
from avaluaproy.programacion_didactica.models import *

#UD10.2

class UnidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = (
            'id',
            '__str__',
        )

class UnidadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = (
            '__all__'
        )

class IEListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstEvaluacion
        fields = (
            'id',
            '__str__',
        )

class IEDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstEvaluacion
        fields = (
            '__all__'
        )

class PondRAListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondRA
        fields = (
            'id',
            '__str__',
        )

class PondRADetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondRA
        fields = (
            '__all__'
        )
        
class PondCEListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondCriterio
        fields = (
            'id',
            '__str__',
        )

class PondCEDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondCriterio
        fields = (
            '__all__'
        )

class PondCEUDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondCritUD
        fields = (
            'id',
            '__str__',
        )

class PondCEUDDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondCritUD
        fields = (
            '__all__'
        )
