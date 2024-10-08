
from .models import Mes, Variacion, VentaArticulo, Total, Indicadores, VentaParticipacion
from django.shortcuts import render

def get_variacion():
    
    return Variacion.objects.select_related('mes').values(
        'mes__mes',
        'variacion_interanual',
        'variacion_intermensual')

def get_venta_articulo():
   
    return VentaArticulo.objects.select_related('mes', 'anio', 'articulo', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'articulo__articulo',
        'tipoPrecio__tipo',
        'total'
    )

def get_venta_total():
   
    return Total.objects.select_related('mes', 'anio', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'tipoPrecio__tipo',
        'venta_total')



def get_indicadores():
   
    return Indicadores.objects.select_related('mes', 'anio').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'cantidad_operaciones',
        'variacion_interanual',
        'variacion_intermensual')


def get_venta_participacion():
   
    return VentaParticipacion.objects.select_related('mes', 'anio', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'tipoPrecio__tipo',
        'acumulado_total')



# Encapsulamiento de logica para la vista final para precios corrientes y constantes

def panel_supermercado(request, tipo_precio, context_keys, template):

    # Consultas iniciales
    meses = Mes.objects.all()
    variacion = get_variacion()
    total = get_venta_total()
    articulos = get_venta_articulo()

    # Inicialización de contextos individuales
    variacion_historico = []
    error_message = None

    # Año y mes por defecto
    anio_default = 6
    mes_default = 1

    # Consultas con valores actuales basadas en el tipo de precio
    variacion_actual = variacion.filter(anio_id=anio_default, tipoPrecio_id=tipo_precio)
    totales = total.filter(anio_id=anio_default, tipoPrecio_id=tipo_precio)
    totales_articulo = articulos.filter(anio_id=anio_default, mes=mes_default, tipoPrecio_id=tipo_precio)

    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        mes = request.POST.get('mes') if request.POST.get('mes') != '0' else mes_default

        if anio == anio_default:
            error_message = "Seleccionar año es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y mes
        if anio != anio_default:
            variacion_historico = variacion.filter(anio_id=anio, tipoPrecio_id=tipo_precio)
            totales = total.filter(anio_id=anio, tipoPrecio_id=tipo_precio)

        if anio != anio_default and mes != mes_default:
            totales_articulo = articulos.filter(anio_id=anio, mes_id=mes, tipoPrecio_id=tipo_precio)

    # Contexto dinámico basado en las claves pasadas como parámetros
    context = {
        'error_message': error_message,
        context_keys['venta_articulo']: totales_articulo,
        context_keys['venta_total']: totales,
        context_keys['variacion']: variacion_actual,
        context_keys['variacion_historico']: variacion_historico,
        'meses': meses,
    }

    # Renderización del template correspondiente
    return render(request, template, context)