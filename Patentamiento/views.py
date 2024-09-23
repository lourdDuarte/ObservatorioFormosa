from django.shortcuts import render
from .models import *

# Create your views here.
def panel_auto(request):
    data_patentamiento = Indicadores.objects.select_related('mes','anio').values(
        'mes__mes',
        'anio__anio',
        'movimiento_vehicular',
        'total',
        'total_acumulado'
    ).filter(tipo_vehiculo_id = 2)
    print(data_patentamiento)
    context = {
        'data_patentamiento': data_patentamiento
    }
    if request.method == "POST":
        año = request.POST.get('año')
       
        
        if año and año.isdigit():
            patentamiento_filtro = Indicadores.objects.select_related('mes').values(
                'mes__mes',
                'movimiento_vehicular_id',
                'variacion_interanual',
                'variacion_intermensual'
            ).filter(tipo_vehiculo_id = 2, movimiento_vehicular_id = 1, anio_id = año)

            transferencia_filtro = Indicadores.objects.select_related('mes').values(
                'mes__mes',
                'movimiento_vehicular_id',
                'variacion_interanual',
                'variacion_intermensual'
            ).filter(tipo_vehiculo_id = 2, movimiento_vehicular_id = 2, anio_id = año)
            
    
            context.update({
                'patentamiento_filtro': patentamiento_filtro,
                'transferencia_filtro': transferencia_filtro
            })
   
    return render (request, 'patentamiento/auto.html', context)