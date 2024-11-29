from .models import *
from django.shortcuts import render

def get_variacion_privado():
    return IndicadoresPrivado.objects.select_related('mes', 'anio','valor',).values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        
        'variacion_interanual',
        'variacion_intermensual'
        
    )


def panel_sector_privado(request,tipo_dato,estacionalidad, context_keys,template):
    meses = Mes.objects.all()
   
    variacion = get_variacion_privado()
   
    # Inicialización de contextos individuales
    variacion_historico = []
    
    
    error_message = None
    error_data = None

    # Año y mes por defecto
    anio_default = 6
    valor_default = 1
    dato_default = tipo_dato
    estacionalidad_default = estacionalidad

    variacion_actual = variacion.filter(anio_id = anio_default, valor_id = valor_default, tipo_id = dato_default, estacionalidad = estacionalidad_default)
   
    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        valor = request.POST.get('valor') if request.POST.get('valor') != '0' else valor_default

        if anio == anio_default and valor == valor_default:
            error_message = "Seleccionar año y valor es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y valor
        if anio != anio_default and valor != valor_default:
            variacion_historico = variacion.filter(anio_id=anio, valor_id = valor, tipo_id = dato_default, estacionalidad = estacionalidad_default)
           
       
           
    context = {
        'error_message': error_message,

        context_keys['variacion']: variacion_actual,
        context_keys['variacion_historico']: variacion_historico,
        'meses':meses
    
    
    }

    return render(request, template, context)