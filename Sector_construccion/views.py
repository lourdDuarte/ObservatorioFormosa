from django.shortcuts import render
from .models import *
from .utils import *

# Create your views here.
def asalariados_construccion(request):
    context_keys = {
        'variacion':'variacion',
        'variacion_historico': 'variacion_historico',
        'sector_construccion':'sector_construccion',
        'sector_construccion_historico': 'construccion_historico'
    }

    return panel_construccion(request, tipo_dato= 1, context_keys=context_keys,template='construccion/asalariados.html' )


def puestos_construccion(request):
    context_keys = {
        'variacion':'variacion',
        'variacion_historico': 'variacion_historico',
        'sector_construccion':'sector_construccion',
        'sector_construccion_historico': 'construccion_historico'
    }

    return panel_construccion(request, tipo_dato= 2, context_keys=context_keys,template='construccion/puestos_trabajo.html' )