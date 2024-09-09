from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from Observatorio.utils import *
from Supermercado.views import *



def panel(request):
    indicadores_supermercado = datos_supermercado_panel()
    context = {
        'indicadores_supermercado': indicadores_supermercado
    }
    print(context)
    return render (request, 'panel.html', context)



def prueba(request):

    return render (request, 'prueba.html')
