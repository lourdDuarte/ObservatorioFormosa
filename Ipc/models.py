from django.db import models
from Año.models import *
from Valor.models import *
from Mes.models import *
from Comparacion_temporal.models import *


# Create your models here.
class TipoDivision(models.Model):
    tipo_division = models.CharField(max_length=200, null=False,blank=False)


    def __str__(self):
        return self.tipo_division
    

class Ipc(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    comparacion_temporal =  models.ForeignKey(ComparacionTemporal, on_delete=models.CASCADE, related_name='+')
    porcentaje = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.porcentaje
    
class Indicadores(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    division_ipc =  models.ForeignKey(TipoDivision, on_delete=models.CASCADE, related_name='+')
    variacion_mensual = models.CharField(max_length=200, null=False, blank=False)
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.variacion_interanual + "-" + self.variacion_mensual