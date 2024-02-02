from django.db import models
# Create your models here.


class Persona(models.Model):

    nombre = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=256)

    class Meta:
        abstract = True


class Localizacion(models.Model):

    direccion = models.CharField(max_length=256)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=128)

    class Meta:
        abstract = True
