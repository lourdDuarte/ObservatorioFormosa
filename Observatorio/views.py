from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from Observatorio.utils import *
from Supermercado.views import *
from Ipc.views import *
from Ipc.models import *



def panel(request):
    indicadores_supermercado = datos_supermercado_panel()
    indicadores_ipc = datos_ipc_panel()
    context = {
        'indicadores_supermercado': indicadores_supermercado,
        'indicadores_ipc': list(indicadores_ipc)
    }
    print(context)
    return render (request, 'panel.html', context)



def prueba(request):

    return render (request, 'prueba.html')


def gestor_consultas(request):
    if request.method == "POST":
        seleccionados = request.POST.getlist('consulta') 
       
        if 'Moto' in seleccionados:
            resultados = Indicadores.objects.select_related('mes','anio','valor').values(
            'mes__mes',
            'anio__anio',
            ).filter(anio_id=2)
            print(resultados)
        if 'Auto' in seleccionados:
            print('Auto')
        if 'Puesto sector construccion' in seleccionados:
            print('Puesto sector construccion')
        if 'Salario sector construccion' in seleccionados:
            print('Salario sector construccion')
        if 'Sector construccion' in seleccionados:
            print('Sector construccion')
            
        if resultados.exists():
            encabezados = list(resultados[0].keys())
            datos = list(resultados)
           
            solo_valores = []
            for fila in datos:
              
                valores = [valor for clave, valor in fila.items()]
                solo_valores.append(valores)

            
            return render(request, 'consultas.html', {
                'encabezados': encabezados,
                'datos': solo_valores
            })
        
    return render(request, 'consultas.html')
    
