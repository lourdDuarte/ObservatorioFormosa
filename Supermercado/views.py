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
        'venta_articulo': 'venta_articulo',
        'venta_total': 'venta_total_corriente',
        'variacion': 'variacion_corriente',
        'variacion_historico': 'variacion_corriente_historico'
    }
    return panel_supermercado(request, tipo_precio=2, context_keys=context_keys, template='Supermercado/panel-corriente.html')

# Panel para precios constantes
def panel_supermercado_constante(request):
    context_keys = {
        'venta_articulo': 'venta_articulo',
        'venta_total': 'venta_total_constante',
        'variacion': 'variacion_constante',
        'variacion_historico': 'variacion_constante_historico'
    }
    return panel_supermercado(request, tipo_precio=1, context_keys=context_keys, template='Supermercado/panel-constante.html')


def index(request):


    valores = Valor.objects.all()

    indicadores = get_indicadores()
    acumulados = get_venta_participacion()
    anio_default = 6
    valor_default = 1

    indicador_actual = indicadores.filter(anio_id = anio_default, valor_id = valor_default)
    

    indicador_historico = []
    error_message = None

    



    operaciones = indicadores.filter(anio_id = anio_default, valor_id = valor_default)
    acumulados = acumulados.filter(anio_id = anio_default,tipoPrecio_id = 2, valor_id = valor_default)

    if request.method == "POST":
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        valor = request.POST.get('valor') if request.POST.get('valor') != '0' else valor_default
        
        if anio == anio_default or valor == valor_default:
            error_message = "Seleccionar año y valor es obligatorio para aplicar filtros"


        if anio != anio_default and valor != valor_default:
            indicador_historico = indicadores.filter(anio_id = anio, valor_id = valor)
           
            operaciones = indicadores.filter(anio_id = anio, valor_id = valor)
            acumulados = acumulados.filter(anio_id = anio,tipoPrecio_id = 2, valor_id = valor_default)

    context = {
        'indicador_actual':indicador_actual,
        'indicador_historico': indicador_historico,
        'acumulados':acumulados,
        'operaciones': operaciones,
        'valores':valores,
        'error_message':error_message
    }



    return render (request, 'Supermercado/index.html', context)