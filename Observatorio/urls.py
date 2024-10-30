"""Observatorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Supermercado import views as supermercado
from Sector_construccion import views as construccion
from Ipc import views as ipc
from Patentamiento import views as patentamiento
from Observatorio import views as observatorio
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', observatorio.panel, name='panel'),
    path('prueba/', observatorio.prueba, name='prueba'),
    path('consulta/', observatorio.gestor_consultas, name='consulta'),

    path('supermercado-corriente/', supermercado.panel_supermercado_corriente, name='supermercado-corriente'),
    path('supermercado-constante/', supermercado.panel_supermercado_constante, name='supermercado-constante'),
   

    path('ipc-inicio/', ipc.ipc, name='ipc-inicio'),

    path('auto-patentamiento/', patentamiento.panel_auto_patentamiento, name='auto-patentamiento'),
    path('auto-transferencia/', patentamiento.panel_auto_transferencia, name='auto-transferencia'),
    
    path('moto-patentamiento/', patentamiento.panel_moto_patentamiento, name='moto-patentamiento'),
    path('moto-transferencia/', patentamiento.panel_moto_transferencia, name='moto-transferencia'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
