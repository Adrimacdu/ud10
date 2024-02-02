from django.db import models
from common.models import Persona, Localizacion
from programacion_didactica.models import Unidad
from core.models import CritEvaluacion, ResAprendizaje, Modulo

# Create your models here.

#UD9.4 Creacion de modelos a partir de clases abstractas

class Alumno(Persona, Localizacion):

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + self.ciudad + " " + self.direccion + " " + self.codigo_postal
    

class CriterioEvalUD(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=False)
    criterio_evaluacion = models.ForeignKey(CritEvaluacion, on_delete=models.PROTECT, null=False )

class CalificacionUDCE(models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False)
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=False)
    crit_evaluacion = models.ForeignKey(CritEvaluacion, on_delete=models.PROTECT, null=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class CalificacionCE(models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False)
    crit_evaluacion = models.ForeignKey(CritEvaluacion, on_delete=models.PROTECT, null=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class CalificacionRA(models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False)
    res_aprendizaje = models.ForeignKey(ResAprendizaje, on_delete=models.PROTECT, null=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class CalificacionTotal(models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=False)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT, null=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True)


