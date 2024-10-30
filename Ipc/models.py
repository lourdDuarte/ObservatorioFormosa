from django.db import models
from Anio.models import *
from Valor.models import *
from Mes.models import *
from Comparacion_temporal.models import *


# Create your models here.
class TipoDivision(models.Model):
    tipo_division = models.CharField(max_length=200, null=False,blank=False)


    def __str__(self):
        return self.tipo_division
    

class Indicadores(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    variacion_intermensual = models.CharField(max_length=200, null=False, blank=False)
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.variacion_interanual) + "-" + str(self.variacion_intermensual)
    
class Indicadores_division(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    division_ipc =  models.ForeignKey(TipoDivision, on_delete=models.CASCADE, related_name='+')
    variacion_intermensual = models.CharField(max_length=200, null=False, blank=False)
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.variacion_interanual) + "-" + str(self.variacion_intermensual)