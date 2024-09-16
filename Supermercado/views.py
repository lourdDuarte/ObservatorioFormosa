from django.shortcuts import render
from Observatorio.utils import *
from Supermercado.models import *

# Create your views here.
def datos_supermercado_panel():
    anio = obtener_anio_actual()
    indicador = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=anio, valor_id=1).order_by('-id').first()
    
    return indicador

def panel_supermercado(request):
    # ************* indicadores actuales **************
    




    return render (request,'Supermercado/panel.html')