from django.shortcuts import render
from Observatorio.utils import *
from Ipc.models import *
# Create your views here.
def datos_ipc_panel():
    anio = obtener_anio_actual()
    indicador = Indicadores.objects.select_related('mes').values(
    'mes__mes',  
    
    ).filter(anio_id=2, valor_id=3).order_by('-id')[:2]

    # indicador_interanual = indicadores.filter(comparacion_temporal_id=2).first()
    # indicador_intermensual = indicadores.filter(comparacion_temporal_id=1).first()  

    return indicador


def panel_ipc(request):
    divisiones = TipoDivision.objects.all()

    context = {
        'divisiones':divisiones
    }

    if request.method == "POST":
        año = request.POST.get('año')
        division = request.POST.get('division')
        print (division, año)
        if año and año.isdigit() and division:
            
            data = Indicadores_division.objects.select_related('mes').values(
            'mes__mes',
            'variacion_intermensual',
            'variacion_interanual'
            ).filter(division_ipc_id = division, anio_id = año, valor_id = 3)
            print (data)
            context.update({
                'division_data': data,
                
            })
    

    return render(request,'Ipc/panel.html',context)