from django.db import models
# Create your models here.
# UD6.3.a


class Unidad (models.Model):



    codigo = models.CharField(max_length = 4, unique=True)
    nombre = models.CharField(max_length = 256, unique=True)

    # UD6.3.b
    def __str__(self):
        return self.codigo + "-" + self.nombre

    class Meta:
        # UD6.4.e
        verbose_name= 'Unidad'
        verbose_name_plural= 'Unidades'
        # UD6.4.f
        ordering= ['id']

class InstEvaluacion (models.Model):



    codigo = models.CharField(max_length=4, unique=True)
    nombre = models.CharField(max_length=256, unique=True)
    descripcion = models.TextField()

    # UD6.3.b
    def __str__(self):
        return self.codigo + "-" + self.nombre

    class Meta:
        # UD6.4.e
        verbose_name='Instrumento Evaluacion'
        verbose_name_plural='Instrumentos Evaluacion'
        # UD6.4.f
        ordering= ['codigo']

class PondRA(models.Model):

    resultado_aprendizaje = models.ForeignKey('core.ResAprendizaje', on_delete=models.PROTECT)
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    # UD6.3.b
    def __str__(self):
        return str(self.resultado_aprendizaje) + "-" + str(self.porcentaje)

    class Meta:
        # UD6.4.e
        verbose_name= 'Ponderacion RA'
        verbose_name_plural= 'Ponderaciones RA'
        # UD6.4.f
        ordering= ['resultado_aprendizaje__codigo']

class PondCriterio (models.Model):

    criterio_evaluacion = models.ForeignKey('core.CritEvaluacion', on_delete=models.PROTECT)
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    # UD6.3.b
    def __str__(self):
        return str(self.criterio_evaluacion.codigo) + "-" + str(self.porcentaje)

    class Meta:
        # UD6.4.e
        verbose_name= 'Ponderacion Criterios'
        verbose_name_plural= 'Ponderaciones Criterios'
        # UD6.4.f
        ordering= ['criterio_evaluacion__codigo']

class PondCritUD (models.Model):


    criterio_evaluacion = models.ForeignKey('core.CritEvaluacion', on_delete=models.PROTECT)
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT)
    porcentaje = models.DecimalField(decimal_places=2, max_digits=5, default=0)

# UD6.3.b_modulo
    def __str__(self):
        return str(self.unidad) + ":" + str(self.criterio_evaluacion) + "' - ('" + str(self.porcentaje) + "')'"

# UD6.3.c
    class Meta:
        unique_together = ('criterio_evaluacion', 'unidad')
        # UD6.4.e
        verbose_name= 'Ponderacion Criterio Unidad'
        verbose_name_plural= 'Ponderaciones Criterio Unidad'
        # UD6.4.f
        ordering= ['unidad__nombre', 'criterio_evaluacion__codigo']
