from rest_framework import serializers, response, status
from programacion_aula.models import *

#UD10.2

class AlumnoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = (
            'id',
            '__str__',
        )

class AlumnoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = (
            '__all__'
        )

class CEUDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriterioEvalUD
        fields = (
            'id',
            '__str__',
        )

class CEUDDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriterioEvalUD
        fields = (
            '__all__'
        )
class CalUDCEListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionUDCE
        fields = (
            'id',
            '__str__',
        )

class CalUDCEDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionUDCE
        fields = (
            '__all__'
        )

class CalCEListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionCE
        fields = (
            'id',
            '__str__',
        )

class CalCEDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionCE
        fields = (
            '__all__'
        )


class CalRAListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionRA
        fields = (
            'id',
            '__str__',
        )

class CalRADetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionRA
        fields = (
            '__all__'
        )

class CalTotalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionTotal
        fields = (
            'id',
            '__str__',
        )

class CalTotalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionTotal
        fields = (
            '__all__'
        )