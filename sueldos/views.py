from django.shortcuts import render
from .models import Liquidacion
from empresa.models import Empresa
# Create your views here.
def liquidaciones_list(request):
    context = {}
    empresa_id = request.session['empresa_id']
    empresa_bbdd = Empresa.objects.get(id=empresa_id)
    if Liquidacion.objects.filter(empresa=empresa_bbdd).exists():
        liquidaciones = Liquidacion.objects.filter(empresa=empresa_bbdd)
        context["liquidaciones"] = liquidaciones
    else:
        pass
    
    return render(request, 'sueldos/liquidaciones_list.html',context=context)