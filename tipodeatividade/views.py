from django.http import HttpResponse
from django.shortcuts import redirect, render
from tipodeatividade.models import Tipodeatividade



# Create your views here.
def listar(request):
    lista_tipos_atividade = Tipodeatividade.objects.all()
    contexto = {
        'tipodeatividade': lista_tipos_atividade
    }
    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

def cadastro(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')

def excluir(request, codigoTipodeatividade):
    try:
        tipo_atividade = Tipodeatividade.objects.get(pk=codigoTipodeatividade)
        tipo_atividade.delete()
    except Tipodeatividade.DoesNotExist:
        pass
    
    return redirect('tipodeatividade:listar')