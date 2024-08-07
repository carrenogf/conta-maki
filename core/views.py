from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from empresa.models import Empresa
class home(TemplateView):
	template_name = "home.html"



def carga_recibo(request,liquidacion,empleado):
	return render(request, 'carga_recibo.html')

