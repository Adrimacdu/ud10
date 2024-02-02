from django.contrib import admin
from .models import *
# Register your models here.

#UD9.4 Admin para crear alumnos, habria que hacer los otros para cada modelo pero no se pide en la practica

class ModAlumno(admin.ModelAdmin):
                                             
    list_display= ['nombre', 'apellidos', 'ciudad', 'codigo_postal', 'direccion'] 
    list_display_links= ['ciudad', 'nombre']
    search_fields= ['ciudad', 'nombre']
    readonly_fields= ['id']


class ModCriterioEvalUD(admin.ModelAdmin):

    list_display= ['unidad'] 
    list_display_links= ['unidad'] 
    search_fields= ['unidad'] 
    readonly_fields= ['id']
    
class ModCalificacionUDCE(admin.ModelAdmin):
    list_display= ['alumno', 'unidad', 'calificacion'] 
    list_display_links= ['alumno', 'unidad'] 
    search_fields= ['alumno', 'unidad' ]
    readonly_fields= ['id']

class ModCalificacionCE(admin.ModelAdmin):
    list_display= ['alumno', 'calificacion'] 
    list_display_links= ['alumno'] 
    search_fields= ['alumno'] 
    readonly_fields= ['id']

class ModCalificacionRA(admin.ModelAdmin):
    list_display= ['alumno',  'res_aprendizaje', 'calificacion'] 
    list_display_links= ['alumno', 'res_aprendizaje'] 
    search_fields= ['alumno', 'res_aprendizaje'] 
    readonly_fields= ['id']

class ModCalificacionTotal(admin.ModelAdmin):
    list_display= ['alumno',  'modulo', 'calificacion'] 
    list_display_links= ['alumno', 'modulo'] 
    search_fields= ['alumno', 'modulo'] 
    readonly_fields= ['id']


admin.site.register(Alumno, ModAlumno)
admin.site.register(CriterioEvalUD, ModCriterioEvalUD)
admin.site.register(CalificacionUDCE, ModCalificacionUDCE)
admin.site.register(CalificacionCE, ModCalificacionCE)
admin.site.register(CalificacionRA, ModCalificacionRA)
admin.site.register(CalificacionTotal, ModCalificacionTotal)
