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
    path('supermercado-inicio/', supermercado.index, name='supermercado-inicio'),
    path('supermercado-corriente/', supermercado.panel_supermercado_corriente, name='supermercado-corriente'),
    path('supermercado-constante/', supermercado.panel_supermercado_constante, name='supermercado-constante'),
   

    path('ipc-panel/', ipc.panel_ipc, name='ipc-panel'),
    path('construccion-panel/', construccion.panel_construccion, name='construccion-panel'),
    path('auto-panel/', patentamiento.panel_auto, name='auto-panel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
