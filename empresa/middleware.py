# empresa/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class EmpresaSeleccionadaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Permite que se procese la vista de selección de empresa
        if request.path == reverse('seleccionar_empresa'):
            response = self.get_response(request)
            return response

        # Si no hay empresa seleccionada, redirige a la vista de selección
        if 'empresa_id' not in request.session:
            return redirect('seleccionar_empresa')

        response = self.get_response(request)
        return response
