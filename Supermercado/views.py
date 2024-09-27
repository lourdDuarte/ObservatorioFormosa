from django.shortcuts import render
from Observatorio.utils import *
from Supermercado.models import *
from Mes.models import *

# Create your views here.
def datos_supermercado_panel():
    anio = obtener_anio_actual()
    indicador = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=anio, valor_id=1).order_by('-id').first()
    
    return indicador

from django.shortcuts import render
from .models import Mes, Variacion, VentaArticulo, Total

def get_variacion(anio_id, tipo_precio_id):
    """Obtiene variaciones filtradas por año y tipo de precio."""
    return Variacion.objects.select_related('mes').values(
        'mes__mes',
        'variacion_interanual',
        'variacion_intermensual'
    ).filter(anio_id=anio_id, tipoPrecio_id=tipo_precio_id)

def get_venta_articulo(anio_id, mes_id, tipo_precio_id):
    """Obtiene ventas de artículos filtradas por año, mes y tipo de precio."""
    return VentaArticulo.objects.select_related('mes', 'anio', 'articulo', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'articulo__articulo',
        'tipoPrecio__tipo',
        'total'
    ).filter(mes_id=mes_id, anio_id=anio_id, tipoPrecio_id=tipo_precio_id)

def get_venta_total(anio_id, tipo_precio_id):
    """Obtiene ventas totales filtradas por año y tipo de precio."""
    return Total.objects.select_related('mes', 'anio', 'tipoPrecio').values(
        'mes__mes',
        'anio__anio',
        'tipoPrecio__tipo',
        'venta_total'
    ).filter(anio_id=anio_id, tipoPrecio_id=tipo_precio_id)

def panel_supermercado(request):
    meses = Mes.objects.all()

    # Consulta inicial para variaciones del año 6
    variacion_corriente = get_variacion(anio_id=6, tipo_precio_id=2)
    variacion_constante = get_variacion(anio_id=6, tipo_precio_id=1)

    # Variables iniciales para los valores históricos
    venta_articulo_corriente = []
    venta_total_corriente = []
    variacion_corriente_historico = {}
    variacion_constante_historico = {}

    if request.method == "POST":
        # Filtros basados en el formulario POST
        anio_id = request.POST.get('año')
        mes_id = request.POST.get('mes')
        tipo_precio_id = request.POST.get('precio')

        # Si hay datos en el formulario, realizamos las consultas específicas
        if anio_id and mes_id and tipo_precio_id:
            venta_articulo_corriente = get_venta_articulo(anio_id=anio_id, mes_id=mes_id, tipo_precio_id=tipo_precio_id)
            venta_total_corriente = get_venta_total(anio_id=anio_id, tipo_precio_id=tipo_precio_id)
            variacion_corriente_historico = get_variacion(anio_id=anio_id, tipo_precio_id=2)
            variacion_constante_historico = get_variacion(anio_id=anio_id, tipo_precio_id=1)
    else:
        # Si no es POST, carga datos por defecto (e.g., mes 1, año 5, tipo de precio 2)
        venta_articulo_corriente = get_venta_articulo(anio_id=5, mes_id=1, tipo_precio_id=2)
        venta_total_corriente = get_venta_total(anio_id=2, tipo_precio_id=2)

    context = {
        'venta_articulo': venta_articulo_corriente,
        'venta_total_corriente': venta_total_corriente,
        'variacion_corriente': variacion_corriente,
        'variacion_constante': variacion_constante,
        'variacion_corriente_historico': variacion_corriente_historico,
        'variacion_constante_historico': variacion_constante_historico,
        'meses': meses,
    }
    return render(request, 'Supermercado/panel.html', context)

    