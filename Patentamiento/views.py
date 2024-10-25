from django.shortcuts import render
from .models import *
from .utils import *

# Create your views here.
def panel_auto_patentamiento(request):
    context_keys = {
        'indicador_actual': 'indicador_actual',
        'indicador_historico': 'indicador_historico',
        'acumulados': 'acumulados',
    }
    
    return panel_vehiculo(request, tipo_vehiculo = 2, tipo_movimiento= 1, context_keys=context_keys, template='patentamiento/auto.html')

def panel_auto_transferencia(request):
    context_keys = {
        'indicador_actual': 'indicador_actual',
        'indicador_historico': 'indicador_historico',
        'acumulados': 'acumulados',
    }
    
    
    return panel_vehiculo(request, tipo_vehiculo = 2, tipo_movimiento= 2, context_keys=context_keys, template='transferencia/auto.html')

def panel_moto_patentamiento(request):
    context_keys = {
        'indicador_actual': 'indicador_moto_actual',
        'indicador_historico': 'indicador_moto_historico',
        'acumulados': 'acumulados',
    }
    
    return panel_vehiculo(request, tipo_vehiculo = 1, tipo_movimiento= 1, context_keys=context_keys, template='patentamiento/moto.html')

def panel_moto_transferencia(request):
    context_keys = {
        'indicador_actual': 'indicador_actual',
        'indicador_historico': 'indicador_historico',
        'acumulados': 'acumulados',
    }
    
    
    return panel_vehiculo(request, tipo_vehiculo = 1, tipo_movimiento= 2, context_keys=context_keys, template='transferencia/moto.html')
