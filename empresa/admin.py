from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('cuit', 'razon_social', 'actividad', 'email')
    search_fields = ('cuit', 'razon_social')
    ordering = ('razon_social',)
    list_per_page = 10
    
    
admin.site.register(Empresa, EmpresaAdmin)