from rest_framework import viewsets, mixins, filters, views
from programacion_aula.api.serializers import *
from programacion_aula.models import Alumno, CriterioEvalUD, CalificacionCE, CalificacionRA, CalificacionTotal, CalificacionUDCE
from rest_framework.exceptions import ValidationError
from .pagination import LargeResultsSetPagination, StandardResultsSetPagination, ShortResultsSetPagination
from rest_framework import serializers, response, status
from rest_framework.decorators import api_view  
from django.http import HttpResponseRedirect
from django.urls import reverse
#UD10.3.b
from programacion_aula.mixins import deleteMixin_api

#UD10.3.a

class AlumnoListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Listado de alumnos 
    """ 
    serializer_class = AlumnoListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'nombre' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['nombre', 'apellidos', 'direccion', 'codigo_postal', 'ciudad']
    
    search_fields = ['nombre', 'apellidos', 'direccion', 'codigo_postal', 'ciudad']

    queryset = Alumno.objects.all()

#UD10.3.b
class AlumnoDetailViewSet(deleteMixin_api,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Si tiene id en la url permite modificar y borrar un alumno, si no la tiene permite crearlo
    """     
    serializer_class = AlumnoDetailSerializer
    queryset = Alumno.objects.all()


    def ready(self) -> None:
        from programacion_aula.signals import crear_calificaciones

#UD10.3.c FALTA COMPROBAR
    #
    #def create(self, request, *args, **kwargs):
     #   response = super().create(request, *args, **kwargs)
     #   if response.status_code == status.HTTP_201_CREATED:
     #       instance = response.data  # Obtener la instancia creada desde la respuesta
     #       criterios_evaluacion = CriterioEvalUD.objects.all()
#
  #          for criterio in criterios_evaluacion:
    #            CalificacionUDCE.objects.create(
     #               alumno=instance,
      #              unidad=criterio.unidad,
       #             crit_evaluacion=criterio.criterio_evaluacion,
        #            calificacion=0
         #       )
        #return response*/



class CEUDListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Listado de criterios de evaluacion por unidad
    """    
    serializer_class = CEUDListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'unidad__nombre' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo_nombre', 
                       'criterio_evaluacion__resultado_aprendizaje_codigo',  
                       'criterio_evaluacion_codigo',
                       'criterio_evaluacion_descripcion', 
                       'unidad_nombre']
    
    search_fields = ['criterio_evaluacion__resultado_aprendizaje__modulo_nombre', 
                       'criterio_evaluacion__resultado_aprendizaje_codigo', 
                       'criterio_evaluacion__resultado_aprendizaje_descripcion', 
                       'criterio_evaluacion_codigo',
                       'criterio_evaluacion_descripcion', 
                       'unidad_nombre']

    def get_queryset(self):
        modulo = self.request.query_params.get('modulo')
        ra = self.request.query_params.get('ra')
        ce = self.request.query_params.get('ce')
        ud = self.request.query_params.get('ud')

        todos = CriterioEvalUD.objects.all()

        if modulo:
            todos.filter(criterio_evaluacion__resultado_aprendizaje__modulo=modulo)
        if ra:
            todos.filter(criterio_evaluacion__resultado_aprendizaje=ra)
        if ce:
            todos.filter(criterio_evaluacion=ce)
        if ud:
            todos.filter(criterio_evaluacion__resultado_aprendizaje=ra)
        
        return todos
    
#UD10.3.b
class CEUDDetailViewSet(deleteMixin_api,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Si tiene id en la url permite modificar y borrar un criterio de evaluacion por unidad, si no la tiene permite crearlo
    """    
    serializer_class = CEUDDetailSerializer
    queryset = CriterioEvalUD.objects.all()

class CalUDCEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Listado de calificaciones de los criterios de evaluacion por unidad
    """    
    serializer_class = CalUDCEListSerializer
    pagination_class = LargeResultsSetPagination
    ordering = 'alumno__nombre' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['unidad_nombre', 
                       'crit_evaluacion__resultado_aprendizaje__modulo_nombre',  
                       'crit_evaluacion__resultado_aprendizaje_codigo',
                       'crit_evaluacion_codigo',
                       'alumno_nombre', 
                       'crit_evaluacion_descripcion']
    
    search_fields = ['unidad_nombre', 
                    'crit_evaluacion__resultado_aprendizaje__modulo_nombre',
                    'crit_evaluacion__resultado_aprendizaje_descripcion',  
                    'crit_evaluacion__resultado_aprendizaje_codigo',
                    'crit_evaluacion_codigo',
                    'alumno_nombre', 
                    'crit_evaluacion_descripcion',
                    'alumno_apellidos']

    def get_queryset(self):
        alumno = self.request.query_params.get('alu')
        ra = self.request.query_params.get('ra')
        modulo = self.request.query_params.get('modulo')
        ce = self.request.query_params.get('ce')
        ud = self.request.query_params.get('ud')
        todos = CalificacionUDCE.objects.all()

        if alumno:
            todos.filter(alumno=alumno)
        if modulo:
            todos.filter(crit_evaluacion__resultado_aprendizaje__modulo=modulo)
        if ra:
            todos.filter(crit_evaluacion__resultado_aprendizaje=ra)
        if ce:
            todos.filter(crit_evaluacion=ce)
        if ud:
            todos.filter(crit_evaluacion__resultado_aprendizaje=ra)
        
        return todos
    
#UD10.3.b
class CalUDCEDetailViewSet(deleteMixin_api,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Si tiene id en la url permite modificar y borrar una calificacion de un criterio de evaluacion por unidad, si no la tiene permite crearlo
    """     
    serializer_class = CalUDCEDetailSerializer
    queryset = CalificacionUDCE.objects.all()

class CalCEListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Listado de calculos de criterios de evaluacion
    """    
    serializer_class = CalCEListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'alumno__nombre' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['crit_evaluacion__resultado_aprendizaje__modulo_nombre',
                        'crit_evaluacion__resultado_aprendizaje_codigo',
                        'crit_evaluacion_codigo', 
                        'alumno_apellidos',
                        'alumno_nombre', 
                        'crit_evaluacion_descripcion']
    
    search_fields = ['crit_evaluacion__resultado_aprendizaje__modulo_nombre', 
                     'crit_evaluacion__resultado_aprendizaje_codigo', 
                     'crit_evaluacion_codigo', 
                     'crit_evaluacion_descripcion', 
                     'alumno_nombre',
                     'alumno_apellidos']

    def get_queryset(self):
        alu = self.request.query_params.get('alu')
        mod = self.request.query_params.get('mod')
        ra = self.request.query_params.get('ra')
        ce = self.request.query_params.get('ce')

        todos = CalificacionCE.objects.all()

        if alu:
            todos.filter(alumno=alu)
        if mod:
            todos.filter(crit_evaluacion__resultado_aprendizaje__modulo=mod)
        if ra:
            todos.filter(crit_evaluacion__resultado_aprendizaje=ra)
        if ce:
            todos.filter(crit_evaluacion=ce)

        return todos
    
#UD10.3.b
class CalCEDetailViewSet(deleteMixin_api,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Si tiene id en la url permite modificar y borrar una califiacion de un criterio de evaluacion, si no la tiene permite crearlo
    """     
    serializer_class = CalCEDetailSerializer
    queryset = CalificacionCE.objects.all()  


class CalRAListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Listado de calculos de los resultados de aprendizaje
    """     
    serializer_class = CalRAListSerializer
    pagination_class = LargeResultsSetPagination
    ordering = 'alumno__nombre' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['res_aprendizaje__modulo_nombre',
                        'res_aprendizaje_codigo',
                        'alumno_apellidos',
                        'alumno_nombre', 
                        'res_aprendizaje_descripcion']
    
    search_fields = ['res_aprendizaje__modulo_nombre',
                        'res_aprendizaje_codigo',
                        'alumno_apellidos',
                        'res_aprendizaje_descripcion']

    def get_queryset(self):
        alu = self.request.query_params.get('alu')
        mod = self.request.query_params.get('mod')
        ra = self.request.query_params.get('ra')

        todos = CalificacionRA.objects.all()

        if alu:
            todos.filter(alumno=alu)
        if mod:
            todos.filter(res_aprendizaje__modulo=mod)
        if ra:
            todos.filter(res_aprendizaje=ra)

        return todos
    
#UD10.3.b
class CalRADetailViewSet(deleteMixin_api,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Si tiene id en la url permite modificar y borrar un resultado de aprendizaje, si no la tiene permite crearlo
    """    
    serializer_class = CalRADetailSerializer
    queryset = CalificacionRA.objects.all()

class CalTotalListViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Listado del calculo total
    """    
    serializer_class = CalTotalListSerializer
    pagination_class = StandardResultsSetPagination
    ordering = 'alumno__nombre' 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['modulo_nombre',
                        'alumno_apellidos',
                        'alumno_nombre']
    
    search_fields = ['modulo_nombre',
                        'alumno_apellidos']

    def get_queryset(self):
        alu = self.request.query_params.get('alu')
        mod = self.request.query_params.get('mod')

        todos = CalificacionTotal.objects.all()

        if alu:
            todos.filter(alumno=alu)
        if mod:
            todos.filter(modulo=mod)

        return todos
    
#UD10.3.b
class CalTotalDetailViewSet(deleteMixin_api,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Si tiene id en la url permite modificar y borrar un calculo total, si no la tiene permite crearlo
    """     
    serializer_class = CalTotalDetailSerializer
    queryset = CalificacionTotal.objects.all()

