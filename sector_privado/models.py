from django.db import models
from Anio.models import *
from Valor.models import *
from Mes.models import *

# Create your models here.
class TipoDato(models.Model):
    tipo = models.CharField(max_length=200, blank=False, null=False)


    def __str__(self):
        return self.tipo
    
class Estacionalidad(models.Model):
    tipo_estacionalidad = models.CharField(max_length=200, blank=False, null=False)


    def __str__(self):
        return self.tipo_estacionalidad
    

class IndicadoresPrivado(models.Model):
    tipo = models.ForeignKey(TipoDato, on_delete=models.CASCADE, related_name='+')
    estacionalidad = models.ForeignKey(Estacionalidad, on_delete=models.CASCADE, related_name='+')
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)
    variacion_intermensual = models.CharField(max_length=200, null=False, blank=False)
    diferencia_interanual = models.CharField(max_length=200, null=False, blank=False)
    diferencia_intermensual = models.CharField(max_length=200, null=False, blank=False)

class CantidadesPrivado(models.Model):
    tipo = models.ForeignKey(TipoDato, on_delete=models.CASCADE, related_name='+')
    estacionalidad = models.ForeignKey(Estacionalidad, on_delete=models.CASCADE, related_name='+')
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    cantidad = models.CharField(max_length=200, null=False, blank=False)

class RamaPrivado(models.Model):
    rama = models.CharField(max_length=200, null=False, blank=False)


class RemuneracionRama(models.Model):
    rama = models.ForeignKey(RamaPrivado, on_delete=models.CASCADE, related_name='+')
    estacionalidad = models.ForeignKey(Estacionalidad, on_delete=models.CASCADE, related_name='+')
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    remuneracion = models.CharField(max_length=200, null=False, blank=False)
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)
    variacion_intermensual = models.CharField(max_length=200, null=False, blank=False)

class AsalariadoRama(models.Model):
    rama = models.ForeignKey(RamaPrivado, on_delete=models.CASCADE, related_name='+')
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE, related_name='+')
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    cantidad = models.CharField(max_length=200, null=False, blank=False)