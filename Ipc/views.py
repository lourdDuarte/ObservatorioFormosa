from django.shortcuts import render
from Observatorio.utils import *
from Ipc.models import *
# Create your views here.
def datos_ipc_panel():
    año = obtener_año_actual()
    indicador_interanual = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'porcentaje').filter(año_id=año, valor_id=3, comparacion_temporal_id = 2).order_by('-id').first()
    
    indicador_intermensual = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'porcentaje').filter(año_id=año, valor_id=3, comparacion_temporal_id = 1).order_by('-id').first()
  