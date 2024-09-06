from django.shortcuts import render
from Observatorio.utils import *
from Supermercado.models import *

# Create your views here.
def datos_supermercado_panel():
    indicador = obtener_consulta_indicadores(Indicadores)
    return indicador