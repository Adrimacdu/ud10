from rest_framework import viewsets, mixins, filters, views
from programacion_didactica.api.serializers import *
from programacion_didactica.models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
from rest_framework.exceptions import ValidationError
from .pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination
from rest_framework import serializers, response, status
from rest_framework.decorators import api_view  

#UD10.3.a

class UnidadListViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = UnidadListSerializer
    pagination_class = None
    ordering = 'nombre'
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nombre']
    search_fields = ['nombre']
    queryset = Unidad.objects.all()

class UnidadDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = UnidadDetailSerializer
    queryset = Unidad.objects.all()


class IEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    serializer_class = UnidadListSerializer
    pagination_class = None
    ordering = 'codigo'
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo','nombre']
    search_fields = ['codigo','nombre', 'descripcion']
    queryset = Unidad.objects.all()

class IEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = IEDetailSerializer
    queryset = InstEvaluacion.objects.all()


class PondRAListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    serializer_class = PondRAListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'resultado_aprendizaje__codigo' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['resultado_aprendizaje__modulo_nombre', 'resultado_aprendizaje_codigo']
    search_fields = ['resultado_aprendizaje__modulo_nombre', 'resultado_aprendizaje_codigo']
    queryset = PondRA.objects.all()

class PondRADetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = PondRADetailSerializer
    queryset = PondRA.objects.all()
    #FALTA HACER VALIDACION UD7 - EJ2 - g


class PondCEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    serializer_class = PondCEListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'criterio_evaluacion__codigo' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo_nombre',
                    'criterio_evaluacion__resultado_aprendizaje_codigo',
                    'criterio_evaluacion_codigo', 
                    'criterio_evaluacion__resultado_aprendizaje_nombre']
    
    search_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo_nombre',
                    'criterio_evaluacion__resultado_aprendizaje__codigo',
                    'criterio_evaluacion__resultado_aprendizaje_nombre',
                    'criterio_evaluacion_codigo',
                    'criterio_evaluacion_descripcion']
    
    queryset = PondCriterio.objects.all()

    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        ra = self.request.query_params.get('res_ap')
        todos = PondCriterio.objects.all()
        if modulo:
            todos = todos.filter(criterio_evaluacion__resultado_aprendizaje__modulo=modulo)
        if ra:
            todos = todos.filter(criterio_evaluacion__resultado_aprendizaje=ra)

        return todos

class PondCEDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = PondCEDetailSerializer
    queryset = PondCriterio.objects.all()
    #FALTA HACER VALIDACION UD7 - EJ2 - g

class PondCEUDListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    serializer_class = PondCEUDListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'criterio_evaluacion__codigo' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['unidad__nombre',
                    'criterio_evaluacion__resultado_aprendizaje__modulo_nombre',
                    'criterio_evaluacion__resultado_aprendizaje_codigo',
                    'criterio_evaluacion_codigo', 
                    'criterio_evaluacion__resultado_aprendizaje_descripcion']
    
    search_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo_nombre',
                    'criterio_evaluacion__resultado_aprendizaje__codigo',
                    'criterio_evaluacion__resultado_aprendizaje_descripcion',
                    'criterio_evaluacion_codigo',
                    'criterio_evaluacion_descripcion',
                    'unidad__nombre']
    
    queryset = PondCritUD.objects.all()

    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        ra = self.request.query_params.get('res_ap')
        ce = self.request.query_params.get('ce')
        ud = self.request.query_params.get('ud')
        todos = PondCritUD.objects.all()

        if modulo:
            todos = todos.filter(criterio_evaluacion__resultado_aprendizaje__modulo=modulo)
        if ra:
            todos = todos.filter(criterio_evaluacion__resultado_aprendizaje=ra)
        if ce:
            todos = todos.filter(criterio_evaluacion=ce)
        if ud:
            todos = todos.filter(unidad=ud)

        return todos
    
class PondCEUDDetailViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = PondCEUDDetailSerializer
    queryset = PondCritUD.objects.all()
    #FALTA HACER VALIDACION UD7 - EJ2 - g