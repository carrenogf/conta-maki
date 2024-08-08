from typing import Any
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from empresa.models import Empresa
from sueldos.models import Liquidacion, Empleado
class home(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		# Liquidaciones
		empresa_id = self.request.session['empresa_id']
		empresa_bbdd = Empresa.objects.get(id=empresa_id)
		if Liquidacion.objects.filter(empresa=empresa_bbdd).exists():
			liquidaciones = Liquidacion.objects.filter(empresa=empresa_bbdd).order_by('-periodo')
			kwargs["liquidaciones"] = liquidaciones[:10]
   
		if Empleado.objects.filter(empresa=empresa_bbdd).exists():
			empleados = Liquidacion.objects.filter(empresa=empresa_bbdd)
			kwargs["empleados"] = empleados
   
   
		return super().get_context_data(**kwargs)