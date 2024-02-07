from programacion_aula.models import Alumno, CalificacionUDCE, CriterioEvalUD
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Alumno)
def crear_calificaciones(sender, instance, **kwargs):
    criterios_evaluacion = CriterioEvalUD.objects.all()

    for criterio in criterios_evaluacion:
        CalificacionUDCE.objects.create(
            alumno=instance,
            unidad=criterio.unidad,
            crit_evaluacion=criterio.criterio_evaluacion
        )
