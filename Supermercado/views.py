from django.shortcuts import render
from Observatorio.utils import *
from Supermercado.models import *
from Mes.models import *
from Valor.models import *
from .utils import *


# Create your views here.
def datos_supermercado_panel():
    anio = obtener_anio_actual()
    indicador = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=anio, valor_id=1).order_by('-id').first()
    
    return indicador


# Panel para precios corrientes
def panel_supermercado_corriente(request):
    context_keys = {
       
        'variacion': 'variacion_corriente',
        'variacion_historico': 'variacion_corriente_historico',
        'venta_articulo':'venta_articulo',
        'venta_total':'venta_total'
       
    }

    return panel_supermercado(request, tipo_precio=2, context_keys=context_keys, template='Supermercado/panel-corriente.html')

# Panel para precios constantes
def panel_supermercado_constante(request):
    context_keys = {
        
        'variacion': 'variacion_constante',
        'variacion_historico': 'variacion_constante_historico',
        'venta_articulo':'venta_articulo',
        'venta_total':'venta_total'
    }
    return panel_supermercado(request, tipo_precio=1, context_keys=context_keys, template='Supermercado/panel-constante.html')





