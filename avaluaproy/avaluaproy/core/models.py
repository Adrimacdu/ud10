from django.db import models


# Create your models here.
# UD6.3.a

class Modulo(models.Model):
    

    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=256, unique=True)
    
    # UD6.3.b
    def __str__(self):
        return self.nombre
    
    # UD6.4.e
    verbose_name= 'Modulo'
    verbose_name_plural= 'Modulos'
    # UD6.4.f
    ordering= ['codigo']



class ResAprendizaje(models.Model):

    modulo = models.ForeignKey(Modulo,on_delete=models.PROTECT)
    codigo = models.CharField(max_length=10)
    descripcion = models.TextField()

    # UD6.3.b
    def __str__(self):
        return self.codigo + "." + self.descripcion[0:100]

    # UD6.3.c
    class Meta:
        unique_together = ('modulo','codigo')
        # UD6.4.e
        verbose_name= 'Resultado Aprendizaje'
        verbose_name_plural= 'Resultados Aprendizaje'
        # UD6.4.f
        ordering= ['codigo']

class CritEvaluacion(models.Model):


    resultado_aprendizaje = models.ForeignKey(ResAprendizaje, on_delete=models.PROTECT, verbose_name='codigo', null=False, blank=False)
    codigo = models.CharField( max_length=4, verbose_name='codigo', null=False, blank=False)
    descripcion = models.TextField( verbose_name='descripcion', null=False, blank=False)
    minimo = models.BooleanField( verbose_name='minimo', null=False, blank=False)

    # UD6.3.b
    def __str__(self):
        return self.resultado_aprendizaje.codigo + "." + self.codigo + "-" + self.descripcion[0:100]
    # UD6.3.c
    class Meta:
        unique_together = ('resultado_aprendizaje', 'codigo')
        # UD6.4.e
        verbose_name= 'Criterio Evaluacion'
        verbose_name_plural= 'Criterios Evaluacion'
        # UD6.4.f
        ordering=['resultado_aprendizaje__codigo', 'codigo']