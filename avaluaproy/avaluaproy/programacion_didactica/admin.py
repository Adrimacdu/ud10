from django.contrib import admin

from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
# Register your models here.

# UD6.4.c
class UnidadAdmin(admin.ModelAdmin):

    list_display= ['codigo', 'nombre']
    list_display_links= ['codigo', 'nombre']
    search_fields= ['codigo', 'nombre']
    ordering= ['-id']
# UD6.4.c
class InstEvalAdmin(admin.ModelAdmin):
    list_display= ['codigo', 'nombre']
    list_display_links= ['codigo', 'nombre']
    search_fields= ['codigo', 'nombre']
# UD6.4.c
class PondRAAdmin(admin.ModelAdmin):
    list_display= ['resultado_aprendizaje', 'porcentaje']
    list_display_links= ['resultado_aprendizaje', 'porcentaje']
    list_filter= ['resultado_aprendizaje']
    search_fields= ['resultado_aprendizaje__codigo','resultado_aprendizaje__descripcion']
    preserve_filters= True
# UD6.4.c
class PondCritAdmin(admin.ModelAdmin):
    list_display= ['criterio_evaluacion', 'porcentaje']
    list_display_links= ['criterio_evaluacion', 'porcentaje']
    list_filter= ['criterio_evaluacion__resultado_aprendizaje']
    search_fields=['criterio_evaluacion', 'criterio_evaluacion__descripcion', 'criterio_evaluacion__resultado_aprendizaje__codigo', 'criterio_evaluacion__resultado_aprendizaje__descripcion']
    preserve_filters= True
# UD6.4.c
class PondCritUDAdmin(admin.ModelAdmin):
    list_display= ['unidad', 'criterio_evaluacion', 'porcentaje']
    list_display_links= ['unidad', 'criterio_evaluacion', 'porcentaje']
    list_filter= ['criterio_evaluacion__resultado_aprendizaje', 'unidad']
    search_fields= ['criterio_evaluacion__codigo','criterio_evaluacion__descripcion', 'criterio_evaluacion__resultado_aprendizaje__codigo', 'criterio_evaluacion__resultado_aprendizaje__descripcion', 'unidad__nombre']
    preserve_filters= True

admin.site.register(Unidad, UnidadAdmin)
admin.site.register(InstEvaluacion, InstEvalAdmin)
admin.site.register(PondRA, PondRAAdmin)
admin.site.register(PondCriterio, PondCritAdmin)
admin.site.register(PondCritUD, PondCritUDAdmin)