from typing import Any

from django.http import HttpResponse
from django.shortcuts import redirect, render
from tipodeatividade.forms import TipodeatividadeForm, TipodeatividadeUpdateForm
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

def carregar_tipodeatividade(request, codigo):
    # recuperar tipo de atividade a ser atualizado
    tipo_atividade = Tipodeatividade.objects.get(pk=codigo)
    contexto = {
        'tipo_atividade': tipo_atividade
    }
    return render(request, 'tipodeatividade/atualizarTiposAtividade.html', context=contexto) 

def atualizar(request):
    # receber form
    form = TipodeatividadeUpdateForm(request.POST)
    # validar form
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        # se ok entao atualizacao

        dados_tipodeatividade: dict[str, Any] = form.cleaned_data
  
        codigo = dados_tipodeatividade['codigo']
        tipo_atividade = Tipodeatividade.objects.get(pk=codigo)

        tipo_atividade.descricao = dados_tipodeatividade['descricao']

        tipo_atividade.save()

# redirect para a pagina de listagem
    return redirect('tipodeatividade:listar')