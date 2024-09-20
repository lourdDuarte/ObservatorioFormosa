from django.shortcuts import render
from Observatorio.utils import *
from Supermercado.models import *

# Create your views here.
def datos_supermercado_panel():
    anio = obtener_anio_actual()
    indicador = Indicadores.objects.select_related('mes').values(
        'mes__mes',  
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=anio, valor_id=1).order_by('-id').first()
    
    return indicador

def panel_supermercado(request):
    # ************* indicadores actuales temporales **************
    
    variacion = Variacion.objects.select_related('mes').values(
        'mes__mes',
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=2, valor_id=1, tipo_precio_id=1)
    
    indicador = Indicadores.objects.select_related('mes').values(
        'mes__mes',
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=2, valor_id=1)

    acumulado = VentaParticipacion.objects.select_related('mes').values(
        'mes__mes',
        'acumulado_total',
        'participacion_total').filter(anio_id=2, valor_id=1)
    
    venta_articulo = VentaArticulo.objects.select_related('mes','anio', 'articulo').values(
        'mes__mes',
        'anio__anio',
        'valor__valor',
        'articulo__articulo',
        'total').filter(tipoPrecio_id=2, valor_id= 1 )
    
    context = {
        'variacion':variacion,
        'venta_articulo':venta_articulo
        # 'indicador': indicador,
        # 'acumulado': acumulado
    }


    return render (request,'Supermercado/panel.html',context)