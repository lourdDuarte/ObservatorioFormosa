from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from Observatorio.utils import *
from Patentamiento.utils import *
from Supermercado.utils import *
from Supermercado.views import *
from Ipc.utils import *
from Ipc.models import *



def panel(request):
   
    
    return render (request, 'panel.html')



def prueba(request):

    return render (request, 'prueba.html')


def consultas(dato, año, valor):
     grafico = None
     if dato == 'Patentamiento - auto':
            indicadores = get_indicadores_vehiculo()
            grafico = indicadores.filter(anio_id=año, valor_id=valor, movimiento_vehicular_id=1, tipo_vehiculo_id=2)
     elif dato == 'Transferencia - auto':
            indicadores = get_indicadores_vehiculo()
            grafico = indicadores.filter(anio_id=año, valor_id=valor, movimiento_vehicular_id=2, tipo_vehiculo_id=2)
     elif dato == 'Patentamiento - moto':
            indicadores = get_indicadores_vehiculo()
            grafico = indicadores.filter(anio_id=año, valor_id=valor, movimiento_vehicular_id=1, tipo_vehiculo_id=1)
     elif dato == 'Transferencia - moto':
            indicadores = get_indicadores_vehiculo()
            grafico = indicadores.filter(anio_id=año, valor_id=valor, movimiento_vehicular_id=2, tipo_vehiculo_id=1)
     elif dato == 'Supermercado - corriente':
            indicadores = get_variacion_supermercado()
            grafico = indicadores.filter(anio_id=año, valor_id=valor, tipoPrecio_id=2)
     elif dato == 'Supermercado - constante':
            indicadores = get_variacion_supermercado()
            grafico = indicadores.filter(anio_id=año, valor_id=valor, tipoPrecio_id=1)
     elif dato == 'Indice precio al consumidor':
            indicadores = get_variacion_ipc()
            grafico = indicadores.filter(anio_id=año, valor_id=valor)
            
     return grafico


def gestor_consultas(request):
    grafico_uno = None  
    grafico_dos = None
    dato_uno = None
    dato_dos = None
    if request.method == "POST":
        # grafico 1
        año_grafico_uno = request.POST.get('año_uno')
        valor_grafico_uno = request.POST.get('valor_uno')
        dato_uno = request.POST.get('dato_uno')

        # grafico 2
        año_grafico_dos = request.POST.get('año_dos')
        valor_grafico_dos = request.POST.get('valor_dos')
        dato_dos = request.POST.get('dato_dos')

        grafico_uno = consultas(dato_uno, año_grafico_uno,valor_grafico_uno)
        grafico_dos = consultas(dato_dos,año_grafico_dos,valor_grafico_dos)
    context = {
        'grafico_uno': grafico_uno, 
        'modelo_uno': dato_uno,
        'grafico_dos': grafico_dos, 
        'modelo_dos': dato_dos,
        
    }
    return render(request, 'consultas.html', context)
