from .models import *
from django.shortcuts import render
from django.db.models import Max

def get_variacion_privado():
    return IndicadoresPrivado.objects.select_related('mes', 'anio','valor').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        
        'variacion_interanual',
        'variacion_intermensual'
        
    )


def get_cantidad_rama():
    

    return AsalariadoRama.objects.select_related('mes', 'anio','valor','rama', 'trimestre').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'rama__rama',
        'trimestre__trimestre',
        'cantidad')


def panel_ramas_asalariados(request,  context_keys,template):
    meses = Mes.objects.all()
    cantidades = get_cantidad_rama()
    error_message = None
    
    cantidades_rama_historico = []
    # Año y mes por defecto
    anio_default = 6
   
    ultimo_trimestre_id = cantidades.filter(anio_id=anio_default).aggregate(Max('trimestre_id'))['trimestre_id__max']

    # Filtrar el registro asociado al trimestre "último" según tu criterio
    cantidades_rama_actual = cantidades.filter(
        anio_id=anio_default,
        trimestre_id=ultimo_trimestre_id
    )

  
    
    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        trimestre = request.POST.get('trimestre') 

        if anio == anio_default and trimestre:
            error_message = "Seleccionar año y trimestre es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y valor
        if anio != anio_default:
           
            cantidades_rama_historico = cantidades.filter(anio_id=anio, trimestre_id = trimestre)
           
    context = {
        'error_message': error_message,
        context_keys['cantidades_rama_actual']: cantidades_rama_actual,
        context_keys['cantidades_rama_historico']: cantidades_rama_historico,
        'meses':meses
    
    
    }

    return render(request, template, context)


def panel_sector_privado(request,tipo_dato,estacionalidad, context_keys,template):
    meses = Mes.objects.all()
   
    variacion = get_variacion_privado()
   
    # Inicialización de contextos individuales
    variacion_historico = []
    
    
    error_message = None
    

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