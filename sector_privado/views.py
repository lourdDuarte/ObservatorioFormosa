from django.shortcuts import render
from .utils import *

# Create your views here.
def evolucion_sector_privado(request):
    context_keys = {
        'variacion':'variacion',
        'variacion_historico': 'variacion_historico'   
    }

    return panel_sector_privado(request, tipo_dato= 1, estacionalidad = 1, context_keys=context_keys,template='privado/evolucion_empleo.html' )


def trabajadores_sector_privado(request):
    context_keys = {
        'variacion':'variacion',
        'variacion_historico': 'variacion_historico'   
    }

    return panel_sector_privado(request, tipo_dato= 1, estacionalidad = 1, context_keys=context_keys,template='privado/trabajadores.html' )
