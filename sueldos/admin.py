from django.contrib import admin
from .models import Empleado, Liquidacion, Recibo, Concepto, DetalleRecibo

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'cuil', 'tipo_liquidacion', 'fecha_ingreso', 'activo')
    list_filter = ('activo', 'tipo_liquidacion')
    search_fields = ('nombre', 'apellido', 'dni', 'cuil')
    ordering = ('nombre', 'apellido')
    list_per_page = 10

class liquidacionAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'periodo', 'abierta')
    list_filter = ('abierta', 'empresa')
    search_fields = ('empresa__razon_social', 'periodo')
    ordering = ('empresa', 'periodo')
    list_per_page = 10
    
class ReciboAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'liquidacion')
    list_filter = ('liquidacion', 'empleado')
    search_fields = ('empleado__nombre', 'empleado__apellido', 'liquidacion__periodo')
    ordering = ('empleado', 'liquidacion')
    list_per_page = 10
    
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo', 'computa_sac')
    list_filter = ('tipo', 'computa_sac')
    search_fields = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')
    list_per_page = 10
    
class DetalleReciboAdmin(admin.ModelAdmin):
    list_display = ('recibo', 'concepto', 'monto')
    list_filter = ('recibo', 'concepto')
    search_fields = ('recibo__empleado__nombre', 'recibo__empleado__apellido', 'concepto__nombre')
    ordering = ('recibo', 'concepto')
    list_per_page = 10
    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Liquidacion, liquidacionAdmin)
admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Concepto, ConceptoAdmin)
admin.site.register(DetalleRecibo, DetalleReciboAdmin)