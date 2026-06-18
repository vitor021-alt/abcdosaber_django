from django.http import HttpResponse
from django.shortcuts import redirect, render
from tipodeatividade.forms import TipodeatividadeForm
from tipodeatividade.models import Tipodeatividade



# Create your views here.
def listar(request):
    lista_tipos_atividade = Tipodeatividade.objects.all()
    contexto = {
        'tipodeatividade': lista_tipos_atividade
    }
    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')

def cadastrar(request):
    form = TipodeatividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = Tipodeatividade(
            descricao = dados_tipodeatividade['descricao']
        )

        tipodeatividade.save()

    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')

def cadastro(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')


def excluir(request, codigoTipodeatividade):
    try:
        tipo_atividade = Tipodeatividade.objects.get(pk=codigoTipodeatividade)
        tipo_atividade.delete()
    except Tipodeatividade.DoesNotExist:
        pass
    
    return redirect('tipodeatividade:listar')