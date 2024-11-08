
from .models import Mes, Variacion, VentaArticulo, Total, Indicadores, VentaParticipacion
from django.shortcuts import render

def get_variacion_supermercado():
    
    return Variacion.objects.select_related('mes','anio','valor' ).values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'variacion_interanual',
        'variacion_intermensual')

def get_venta_articulo():
   
    return VentaArticulo.objects.select_related('mes', 'anio','valor', 'articulo', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'articulo__articulo',
        'tipoPrecio__tipo',
        'total'
    ).order_by( '-anio', 'mes','articulo','valor')


def get_venta_total():
   
    return Total.objects.select_related('mes', 'anio', 'valor', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'tipoPrecio__tipo',
        'venta_total').order_by( '-anio', 'mes','valor')




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
        'valor__valor',
        'tipoPrecio__tipo',
        'acumulado_total')



# Encapsulamiento de logica para la vista final para precios corrientes y constantes

def panel_supermercado(request, tipo_precio, context_keys, template):

    # Consultas iniciales
    meses = Mes.objects.all()
    variacion = get_variacion_supermercado()
    venta_articulo = get_venta_articulo().filter(tipoPrecio_id=tipo_precio)
    venta_total = get_venta_total().filter(tipoPrecio_id=tipo_precio)
    
    
    # Inicialización de contextos individuales
    variacion_historico = []
    error_message = None

    # Año y mes por defecto
    anio_default = 6
    valor_default = 1

    # Consultas con valores actuales basadas en el tipo de precio
    variacion_actual = variacion.filter(anio_id=anio_default, tipoPrecio_id=tipo_precio, valor_id = valor_default)
    

    if request.method == 'POST':
        # Validación de filtros recibidos en el formulario
        anio = request.POST.get('año') if request.POST.get('año') != '0' else anio_default
        valor = request.POST.get('valor') if request.POST.get('valor') != '0' else valor_default

        if anio == anio_default and valor == valor_default:
            error_message = "Seleccionar año y valor es obligatorio para aplicar filtros"

        # Aplicación de filtros en función de año y valor
        if anio != anio_default and valor != valor_default:
            variacion_historico = variacion.filter(anio_id=anio, tipoPrecio_id=tipo_precio, valor_id = valor)
            

        

    # Contexto dinámico basado en las claves pasadas como parámetros
    context = {
        'error_message': error_message,
        context_keys['variacion']: variacion_actual,
        context_keys['variacion_historico']: variacion_historico,
        context_keys['venta_articulo']: venta_articulo,
        context_keys['venta_total']: venta_total,
        'meses': meses,
    }

    # Renderización del template correspondiente
    return render(request, template, context)