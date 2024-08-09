from django.shortcuts import render
from django.shortcuts import render, redirect
from empresa.models import Empresa

def seleccionar_empresa(request):
    # Funcion para mantener una empresa seleccionada en la sesion
    if request.method == 'POST':
        empresa_id = request.POST.get('empresa')
        request.session['empresa_id'] = empresa_id
        request.session['empresa_razon_social'] = Empresa.objects.get(pk=empresa_id).razon_social
        return redirect(request.META.get('HTTP_REFERER'))
    
    empresas = Empresa.objects.all()
    return render(request, 'empresa/select_empresa.html', {'empresas': empresas})