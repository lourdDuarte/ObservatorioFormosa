from Anio.models import Anio
from Valor.models import Valor
from Mes.models import Mes
from datetime import *

def obtener_anio_actual():
    now = datetime.now()
    
    anio = Anio.objects.values('id').filter(anio = now.strftime('%Y')).first()
    
    return(anio['id'])


def obtener_consulta_indicadores(modelo):
    anio = obtener_anio_actual()
    indicadores = modelo.objects.select_related('mes').values(
        'mes__mes',  # Supongamos que 'nombre' es el campo que quieres del modelo Mes
        'variacion_interanual',
        'variacion_intermensual').filter(anio_id=anio, valor_id=1).order_by('-id').first()
    return indicadores