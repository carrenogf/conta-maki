from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Liquidacion, Empleado
from empresa.models import Empresa
from typing import Any
# Create your views here.
class sueldos_home(TemplateView):
	template_name = "sueldos/sueldos_home.html"

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		# Liquidaciones
		empresa_id = self.request.session['empresa_id']
		empresa_bbdd = Empresa.objects.get(id=empresa_id)
		if Liquidacion.objects.filter(empresa=empresa_bbdd).exists():
			liquidaciones = Liquidacion.objects.filter(empresa=empresa_bbdd).order_by('-periodo')
			kwargs["liquidaciones"] = liquidaciones[:10]
   
		if Empleado.objects.filter(empresa=empresa_bbdd).exists():
			empleados = Empleado.objects.filter(empresa=empresa_bbdd)
			kwargs["empleados"] = empleados
   
   
		return super().get_context_data(**kwargs)