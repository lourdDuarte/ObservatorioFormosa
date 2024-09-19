from django.shortcuts import render
from .models import *

# Create your views here.
def panel_construccion(request):
    tipo_datos = TipoDato.objects.all()

    context = {
        'tipo_datos':tipo_datos
    }

    if request.method == "POST":
        año = request.POST.get('año')
        tipo_dato = request.POST.get('tipo_dato')
        
        if año and año.isdigit() and tipo_dato:
            
            data = Indicadores.objects.select_related('mes').values(
            'mes__mes',
            'variacion_intermensual',
            'variacion_interanual'
            ).filter(tipo_dato_id = tipo_dato, anio_id = año, valor_id = 1)
            print (data)
            context.update({
                'indicadores_data': data,
                
            })
    return render(request, 'construccion/panel.html', context)