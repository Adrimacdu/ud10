from django.contrib import admin

from .models import Modulo, ResAprendizaje, CritEvaluacion
# Register your models here.

# UD6.4.b
class ModAdmin(admin.ModelAdmin):
                                             # UD6.4.a
    list_display= ['id', 'codigo', 'nombre'] # se utiliza para especificar qué campos deben mostrarse como columnas en la vista de lista de los objetos en el panel de administración
    list_display_links= ['codigo', 'nombre']
    search_fields= ['codigo', 'nombre']
    readonly_fields= ['id']
# UD6.4.b
class ResAprendizajeAdmin(admin.ModelAdmin):

    list_display= ['codigo', 'modulo', 'descripcion']
    list_display_links= ['codigo', 'modulo', 'descripcion']
    list_filter= ['modulo']
    search_fields= ['codigo', 'descripcion']
    preserve_filters= True
# UD6.4.b
class CritEvaluacionAdmin(admin.ModelAdmin):

    list_display= ['resultado_aprendizaje', 'codigo', 'descripcion', 'minimo']
    list_display_links= ['resultado_aprendizaje', 'codigo', 'descripcion', 'minimo']
    list_filter= ['resultado_aprendizaje', 'minimo']
    search_fields= ['codigo', 'resultado_aprendizaje', 'descripcion']
    preserve_filters= True

admin.site.register(Modulo, ModAdmin)
admin.site.register(ResAprendizaje, ResAprendizajeAdmin)
admin.site.register(CritEvaluacion, CritEvaluacionAdmin)