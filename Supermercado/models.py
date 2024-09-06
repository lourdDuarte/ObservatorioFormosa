from django.db import models
from Año.models import *
from Valor.models import *
from Mes.models import *
from Comparacion_temporal.models import *




class TipoPrecio(models.Model):
    tipo = models.CharField(max_length=200, blank=False,null=False)

    def __str__(self):
        return self.tipo

class TipoArticulo(models.Model):
    tipo_articulo = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.tipo_articulo

class Total(models.Model):
     año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
     mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
     valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
     tipoPrecio = models.ForeignKey(TipoPrecio, on_delete=models.CASCADE, related_name='+')
     venta_total = models.CharField(max_length=200,null=False,blank=False)

     def __str__(self):
        return self.venta_total

class Variacion(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    comparacion_temporal =  models.ForeignKey(ComparacionTemporal, on_delete=models.CASCADE, related_name='+')
    tipoPrecio = models.ForeignKey(TipoPrecio, on_delete=models.CASCADE, related_name='+')
    variacion_porcentual = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.variacion_porcentual


class VentaArticulo(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    articulo_supermercado =  models.ForeignKey(TipoArticulo, on_delete=models.CASCADE, related_name='+')
    tipoPrecio = models.ForeignKey(TipoPrecio, on_delete=models.CASCADE, related_name='+')
    total = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.articulo_supermercado + "-" + self.total


class VentaParticipacion(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    tipoPrecio = models.ForeignKey(TipoPrecio, on_delete=models.CASCADE, related_name='+')
    acumulado_total = models.CharField(max_length=200, null=False, blank=False)
    participacion_total = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.acumulado_total + "-" + self.participacion_total
    
class Indicadores(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, related_name='+')
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE, related_name='+')
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, related_name='+')
    cantidad_operaciones = models.CharField(max_length=200, null=False, blank=False)
    variacion_interanual = models.CharField(max_length=200, null=False, blank=False)
    variacion_intermensual = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.año) + " - " + str(self.mes) + " - " + str(self.valor) + " - " + self.variacion_interanual + " - " + self.variacion_intermensual