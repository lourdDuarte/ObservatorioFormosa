from django.db import models
from Año.models import *
from Valor.models import *
from Mes.models import *

# Create your models here.

class TipoDato(models.Model):
    tipo_dato = models.CharField(max_length=200, blank=False, null=False)

    def __str__ (self):
        return self.tipo_dato
    

class SectorConstruccion(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    total_empresas = models.CharField(max_length=200, blank=False, null=False)
    total_puesto_trabajo = models.CharField(max_length=200, blank=False, null=False)
    salario_promedio = models.CharField(max_length=200, blank=False, null=False)


class Indicadores(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    tipo_dato = models.ForeignKey(TipoDato, on_delete=models.CASCADE, related_name='+')
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)
    variacion_intermensual = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.variacion_interanual + "-" + self.variacion_intermensual