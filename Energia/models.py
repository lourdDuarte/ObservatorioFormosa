from django.db import models
from Anio.models import *
from Valor.models import *
from Mes.models import *
# Create your models here.

class Tarifa(models.Model):
    tarifa = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.tarifa
    
class Demanda(models.Model):
    demanda = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.demanda

class RefsaUsuario(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE, related_name='+')
    cantidad_usuario = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
            return str(self.anio) + " " + self.mes + " " + self.tarifa + " " + str(self.cantidad_usuario)
class RefsaUsuarioVariacion(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE, related_name='+')
    variacion_bimestral = models.CharField(max_length=200,blank=False,null=False)
    variacion_anual = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
            return str(self.anio) + " " + self.mes + " " + self.tarifa + " " + str(self.variacion_bimestral) + " " + str(self.variacion_anual)

class CammesaDemanda(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE, related_name='+')
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE, related_name='+')
    cantidad = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
            return str(self.anio) + " " + self.mes + " " + self.tarifa + " " + str(self.cantidad) 


class CammesaVarDemanda(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE, related_name='+')
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE, related_name='+')
    variacion_mensual = models.CharField(max_length=200,blank=False,null=False)
    variacion_anual = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
            return str(self.anio) + " " + self.mes + " " + self.tarifa + " " + str(self.variacion_mensual) + " " + str(self.variacion_anual)
