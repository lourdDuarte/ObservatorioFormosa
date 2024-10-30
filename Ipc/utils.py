from .models import Mes, Indicadores, Indicadores_division
from django.shortcuts import render


def get_variacion_ipc():
    return Indicadores.objects.select_related('mes', 'valor', 'anio').values(
        'mes__mes',
        'valor__valor',
        'anio__anio',
        'variacion_intermensual',
        'variacion_interanual')


def get_variacion_ipc_division():
    return Indicadores_division.objects.select_related('mes', 'valor', 'anio').values(
        'mes__mes',
        'valor__valor',
        'anio__anio',
        'variacion_intermensual',
        'variacion_interanual').order_by( '-anio', 'mes','valor')


def panel_ipc(request,  context_keys, template):
    meses = Mes.objects.all()
    variacion = get_variacion_ipc()
    ipc_division = get_variacion_ipc_division()

     # Inicialización de contextos individuales
    variacion_historico = []
    error_message = None

    # Año y mes por defecto
    anio_default = 6
    valor_default = 3

    variacion_actual = variacion.filter(anio_id=anio_default, valor_id = valor_default)
    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        valor = request.POST.get('valor') if request.POST.get('valor') != '0' else valor_default

        if anio == anio_default and valor == valor_default:
            error_message = "Seleccionar año y valor es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y valor
        if anio != anio_default and valor != valor_default:
            variacion_historico = variacion.filter(anio_id=anio, valor_id = valor)


    # Contexto dinámico basado en las claves pasadas como parámetros
    context = {
        'error_message': error_message,
        context_keys['variacion']: variacion_actual,
        context_keys['variacion_historico']: variacion_historico,
        context_keys['ipc_division']: ipc_division,
        'meses': meses,
    }

    # Renderización del template correspondiente
    return render(request, template, context)