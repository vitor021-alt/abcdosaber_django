from typing import Any

from django.http import HttpResponse
from django.shortcuts import redirect, render
from instrutor.forms import InstrutorForm, InstrutorUpdateForm
from instrutor.models import Instrutor
from titulo.models import Titulo

# Create your views here.
def listar(request):
    lista_instrutores = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutores
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def carregar_cadastro(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        "titulos": lista_titulos
    }
    return render(request, 'instrutor/cadastroInstrutor.html', context=contexto)

def cadastrar(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(
            nome = dados_instrutor['nome'],
            rg = dados_instrutor['rg'],
            dataNascimento = dados_instrutor['dataNascimento'],
            ddd = dados_instrutor['ddd'],
            telefone = dados_instrutor['telefone'],
            codigo_titulo = dados_instrutor['codigo_titulo']
        )
        
        instrutor.save()
        return redirect('instrutor:listar')

    else:
        erros = form.errors
        contexto = {
            'erros': erros
        }
        
        return render(request, 'instrutor/pagina_erro.html', context=contexto)

def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def excluir(request, codigoInstrutor):
    try:
        instrutor = Instrutor.objects.get(pk=codigoInstrutor)
        instrutor.delete()
    except Instrutor.DoesNotExist:
        pass

def carregar_instrutor(request, codigo):
    # recuperar instrutor a ser atualizado
    instrutor = Instrutor.objects.get(pk=codigo)
    contexto = {
        'instrutor': instrutor
    }
    return render(request, 'instrutor/atualizarInstrutor.html', context=contexto) 

def atualizar(request):
    # receber form
    form = InstrutorUpdateForm(request.POST)
    # validar form
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        # se ok entao atualizacao

        dados_instrutor: dict[str, Any] = form.cleaned_data
  
        codigo = dados_instrutor['codigo']
        instrutor = Instrutor.objects.get(pk=codigo)

        instrutor.nome = dados_instrutor['nome']
        instrutor.rg = dados_instrutor['rg']
        instrutor.dataNascimento = dados_instrutor['dataNascimento']
        instrutor.ddd = dados_instrutor['ddd']
        instrutor.telefone = dados_instrutor['telefone']
        instrutor.codigo_titulo = dados_instrutor['codigo_titulo']

        instrutor.save()

# redirect para a pagina de listagem
    return redirect('instrutor:listar')   