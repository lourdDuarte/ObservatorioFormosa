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

    
    resultados = Ipc.objects.filter(año_id=2).values()
    
    if resultados.exists():
        encabezados = list(resultados[0].keys())
        datos = list(resultados)
        # Para obtener solo los valores de cada registro, excluyendo 'id'
        solo_valores = []
        for fila in datos:
            # Extraer solo los valores de los campos, excluyendo 'id'
            valores = [valor for clave, valor in fila.items() if clave != 'id']
            solo_valores.append(valores)

        print(encabezados)
        print("***********************************")
        print(solo_valores)
        return render(request, 'consultas.html', {
            'encabezados': encabezados,
            'datos': solo_valores
        })
    else:
        return render(request, 'consultas.html', {
            'encabezados': [],
            'datos': []
        })
    
    
