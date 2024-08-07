from .models import Empresa

def empresas(request):
    return {
        'empresas': Empresa.objects.all()
    }