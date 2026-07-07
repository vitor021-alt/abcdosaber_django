from typing import Any

from django.http import HttpResponse
from django.shortcuts import redirect, render
from aluno.forms import AlunoForm, AlunoUpdateForm
from aluno.models import Aluno 

# Create your views here.
def listar(request):
    lista_alunos = Aluno.objects.all()
    contexto = {
        'alunos': lista_alunos
    }
    return render(request, 'aluno/listarAlunos.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'aluno/cadastroAluno.html')

def cadastrar(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        dados_aluno = form.cleaned_data
        aluno = Aluno(
            descricao = dados_aluno['descricao']
        )

        aluno.save()

    return render(request, 'aluno/cadastroAluno.html')


def cadastro(request):
    return render(request, 'aluno/cadastroAluno.html')

def excluir(request, codigoAluno):
    try:
        aluno = Aluno.objects.get(matricula=codigoAluno)
        aluno.delete()
    except Aluno.DoesNotExist:
        pass
    
    return redirect('aluno:listar')

def carregar_aluno(request, codigo):
    # recuperar aluno a ser atualizado
    aluno = Aluno.objects.get(pk=codigo)
    contexto = {
        'aluno': aluno
    }
    return render(request, 'aluno/atualizarAluno.html', context=contexto) 

def atualizar(request):
    # receber form
    form = AlunoUpdateForm(request.POST)
    # validar form
    if form.is_valid():
        dados_aluno = form.cleaned_data
        # se ok entao atualizacao

        dados_aluno = form.cleaned_data
  
        codigo = dados_aluno['codigo']
        aluno = Aluno.objects.get(pk=codigo)

        aluno.descricao = dados_aluno['descricao']

        aluno.save()

# redirect para a pagina de listagem
    return redirect('aluno:listar')