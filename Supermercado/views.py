from django.shortcuts import render
from Observatorio.utils import *
from Supermercado.models import *

# Create your views here.
def datos_supermercado_panel():
    año = obtener_año_actual()
    indicador = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'variacion_interanual',
        'variacion_intermensual').filter(año_id=año, valor_id=1).order_by('-id').first()
    
    return indicador