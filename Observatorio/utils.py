from Año.models import Año
from Valor.models import Valor
from Mes.models import Mes
from datetime import *

def obtener_año_actual():
    now = datetime.now()
    
    año = Año.objects.values('id').filter(año = now.strftime('%Y')).first()
    
    return(año['id'])


def obtener_consulta_indicadores(modelo):
    año = obtener_año_actual()
    indicadores = modelo.objects.select_related('mes').values(
        'mes__mes',  # Supongamos que 'nombre' es el campo que quieres del modelo Mes
        'variacion_interanual',
        'variacion_intermensual').filter(año_id=año, valor_id=1).order_by('-id').first()
    return indicadores