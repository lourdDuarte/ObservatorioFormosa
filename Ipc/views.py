from django.shortcuts import render
from Observatorio.utils import *
from Ipc.models import *
from .utils import *
# Create your views here.
def datos_ipc_panel():
    anio = obtener_anio_actual()
    indicador = Indicadores.objects.select_related('mes').values(
    'mes__mes',  
    
    ).filter(anio_id=2, valor_id=3).order_by('-id')[:2]

  

    return indicador

def ipc(request):
    context_keys = {
        'variacion': 'variacion',
        'variacion_historico': 'variacion_historico',
        'ipc_division':'ipc_division',
    }
    
    return panel_ipc(request,  context_keys=context_keys, template='Ipc/ipc-inicio.html')




   