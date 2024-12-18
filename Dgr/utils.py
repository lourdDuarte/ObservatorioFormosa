from .models import Mes, Indicadores, Recaudacion
from django.shortcuts import render




def get_recaudacion():
    return Recaudacion.objects.select_related('mes', 'valor', 'anio').exclude(tipo_id=4).values(
         'mes__mes',
         'valor__valor',
         'anio__anio',
         'tipo',
         'recaudacion')


def panel_dgr(request,  context_keys, template):
   
    meses = Mes.objects.all()
    recaudacion = get_recaudacion()
    
    recaudacion_historico = []
    error_message = None

    # Año y mes por defecto
    anio_default = 6
    valor_default = 1

    recaudacion_actual = recaudacion.filter(anio_id = anio_default, valor_id = valor_default)
    
    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default

        if anio == anio_default:
            error_message = "Seleccionar año es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y valor
        if anio != anio_default:
            recaudacion_historico = recaudacion.filter(anio_id= anio, valor_id = valor_default)


    # Contexto dinámico basado en las claves pasadas como parámetros
    context = {
        'error_message': error_message,
        context_keys['recaudacion_actual']: recaudacion_actual,
        context_keys['recaudacion_historico']: recaudacion_historico,
       
        'meses': meses,
    }

    # Renderización del template correspondiente
    return render(request, template, context)
