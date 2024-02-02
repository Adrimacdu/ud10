from rest_framework import viewsets, mixins, filters, views
from core.api.serializers import *
from core.models import Modulo, ResAprendizaje
from rest_framework.exceptions import ValidationError
from .pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination
from rest_framework import serializers, response, status
from rest_framework.decorators import api_view

#UD11.3.a

class ModuloListViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = ModuloListSerializer
    pagination_class = None
    ordering = 'codigo'
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']
    queryset = Modulo.objects.all()
    
class ModuloDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = ModuloDetailSerializer
    queryset = Modulo.objects.all()

###############################################


class RAListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = RAListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'codigo'
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo']
    search_fields = ['codigo', 'descripcion']
    
    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        if modulo:
            return ResAprendizaje.objects.filter(modulo=modulo)
        
        return ResAprendizaje.objects.all()

class RADetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = RADetailSerializer
    queryset = ResAprendizaje.objects.all()

###############################################
    
class CEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = CEListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'codigo'
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filter_fields = ['resultado_aprendizaje_modulo', 'resultado_aprendizaje']
    ordering_fields = ['codigo', 'descripcion']
    search_fields = ['codigo', 'descripcion',
                    'resultado_aprendizaje_codigo',
                    'resultado_aprendizaje_descripcion',
                    'resultado_aprendizaje_modulo__nombre']
    
    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        ra = self.request.query_params.get('res_ap')
        if modulo and ra:
            return CritEvaluacion.objects.filter(resultado_aprendizaje__modulo=modulo).filter(resultado_aprendizaje=ra)
        
        return CritEvaluacion.objects.all()

class CEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = CEDetailSerializer
    queryset = ResAprendizaje.objects.all()

###############################################
    

