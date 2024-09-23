from django.shortcuts import render
from .models import *

# Create your views here.
def panel_auto(request):
    data_patentamiento = Indicadores.objects.select_related('mes','anio').values(
        'mes__mes',
        'anio__anio',
        'movimiento_vehicular_id',
        'total',
        'total_acumulado'
    ).filter(tipo_vehiculo_id = 2)

    if request.method == "POST":
        año = request.POST.get('año')
        
        if año and año.isdigit():
            patentamiento_filtro = 

    context = {
        'data_patentamiento': data_patentamiento
    }
   
    return render (request, 'patentamiento/auto.html', context)