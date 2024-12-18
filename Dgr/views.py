from django.shortcuts import render
from .utils import *

# Create your views here.

def view_dgr(request):
    context_keys = {
        'recaudacion_actual':'recaudacion_actual',
        'recaudacion_historico': 'recaudacion_historico'
    }
    return panel_dgr(request,  context_keys=context_keys, template='dgr/recaudacion.html')
