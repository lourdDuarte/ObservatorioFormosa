from django.shortcuts import render

from .models import *
from .utils import *
# Create your views here.
def panel_transferencias(request):
    context_keys = {
        'transferencia_actual': 'transferencia_actual',
        'transferencia_historico': 'transferencia_historico'
        
    }
    
    
    return panel_transferencia(request,  context_keys=context_keys, template='trasnferencia_coparticipacion/transferencia.html')
