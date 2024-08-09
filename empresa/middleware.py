# empresa/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from empresa.models import Empresa

class EmpresaSeleccionadaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Permite que se procese la vista de selección de empresa
        if request.path == reverse('seleccionar_empresa'):
            response = self.get_response(request)
            return response

        # Si no hay empresa seleccionada,selecciona la primera
        if 'empresa_id' not in request.session:
            request.session['empresa_id'] = Empresa.objects.first().id
            request.session['empresa_razon_social'] = Empresa.objects.first().razon_social


        response = self.get_response(request)
        return response
