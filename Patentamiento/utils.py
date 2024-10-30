
from .models import *
from django.shortcuts import render



def get_indicadores_vehiculo():
   
    return Indicadores.objects.select_related('mes', 'anio').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'variacion_interanual',
        'variacion_intermensual')


def get_acumulados_vehiculo():
   
    return Indicadores.objects.select_related('mes', 'anio').values(
        'anio__anio',
        'mes__mes',
        'valor__valor',
        'total',
        'total_acumulado').order_by( '-anio', 'mes','valor')



# Encapsulamiento de logica para la vista final para precios corrientes y constantes

def panel_vehiculo(request, tipo_vehiculo, tipo_movimiento, context_keys, template):

    # Consultas iniciales
    meses = Mes.objects.all()
    indicadores = get_indicadores_vehiculo()
    acumulados = get_acumulados_vehiculo().filter(movimiento_vehicular_id = tipo_movimiento,
                                                 tipo_vehiculo_id = tipo_vehiculo)
    
   
    # Inicialización de contextos individuales
    indicador_historico = []
    error_message = None

    # Año y mes por defecto
    anio_default = 6
    valor_default = 1


    # Consultas con valores actuales basadas en el tipo de precio
    indicadores_actuales = indicadores.filter(anio_id=anio_default, 
                                                          valor_id = valor_default, 
                                                          movimiento_vehicular_id = tipo_movimiento,
                                                          tipo_vehiculo_id = tipo_vehiculo)

    

    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        valor = request.POST.get('valor') if request.POST.get('valor') != '0' else valor_default

        if anio == anio_default or valor == valor_default:
            error_message = "Seleccionar año y valor es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y mes
        if anio != anio_default and valor != valor_default:
            
            indicador_historico = indicadores.filter(anio_id=anio,valor_id = valor, movimiento_vehicular_id = tipo_movimiento,tipo_vehiculo_id = tipo_vehiculo)
            

        
    # Contexto dinámico basado en las claves pasadas como parámetros
    context = {
        'error_message': error_message,
        context_keys['indicador_actual']: indicadores_actuales,
        context_keys['indicador_historico']: indicador_historico,
        context_keys['acumulados']: acumulados,
        'meses':meses,
    }
   
    # Renderización del template correspondiente
    return render(request, template, context)