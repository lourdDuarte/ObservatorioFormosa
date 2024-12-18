from .models import Mes, Transferencia
from django.shortcuts import render



def get_transferencia():
    return Transferencia.objects.select_related('mes', 'valor', 'anio').values(
         'mes__mes',
         'valor__valor',
         'anio__anio',
         'variacion_anual_nominal',
         'variacion_anual_real')



def panel_transferencia(request,  context_keys, template):
    meses = Mes.objects.all()
    transferencia = get_transferencia()
    transferencia_historico = []
    error_message = None

    # Año y mes por defecto
    anio_default = 6
    valor_default = 1

    transferencia_actual = transferencia.filter(anio_id = anio_default, valor_id = valor_default)
    
    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        valor = request.POST.get('valor') if request.POST.get('valor') != '0' else valor_default
        
        if anio == anio_default or valor == valor_default:
            error_message = "Seleccionar año y valor es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y valor
        if anio != anio_default and valor != valor_default:
            transferencia_historico = transferencia.filter(anio_id= anio, valor_id = valor)


    # Contexto dinámico basado en las claves pasadas como parámetros
    context = {
        'error_message': error_message,
        context_keys['transferencia_actual']: transferencia_actual,
        context_keys['transferencia_historico']: transferencia_historico,
       
        'meses': meses,
    }

    # Renderización del template correspondiente
    return render(request, template, context)