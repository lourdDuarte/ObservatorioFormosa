from django.shortcuts import render
from Observatorio.utils import *
from Ipc.models import *
# Create your views here.
def datos_ipc_panel():
    año = obtener_año_actual()
    indicador = Indicadores.objects.select_related('mes').values(
    'mes__mes',  
    
    ).filter(año_id=2, valor_id=3).order_by('-id')[:2]

    # indicador_interanual = indicadores.filter(comparacion_temporal_id=2).first()
    # indicador_intermensual = indicadores.filter(comparacion_temporal_id=1).first()  

    return indicador