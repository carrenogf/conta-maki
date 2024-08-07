from django.shortcuts import render
from django.shortcuts import render, redirect
from empresa.models import Empresa

def seleccionar_empresa(request):
    if request.method == 'POST':
        empresa_id = request.POST.get('empresa')
        request.session['empresa_id'] = empresa_id
        return redirect(request.META.get('HTTP_REFERER'))
    
    empresas = Empresa.objects.all()
    return render(request, 'empresa/select_empresa.html', {'empresas': empresas})