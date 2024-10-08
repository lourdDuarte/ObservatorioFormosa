from django.contrib import admin

from .models import *
# Register your models here.




class VentaArticuloAdmin(admin.ModelAdmin):
    search_fields = ['total']

admin.site.register(TipoPrecio)
admin.site.register(TipoArticulo)
admin.site.register(Total)
admin.site.register(Variacion)
admin.site.register(VentaArticulo, VentaArticuloAdmin)
admin.site.register(VentaParticipacion)
admin.site.register(Indicadores )