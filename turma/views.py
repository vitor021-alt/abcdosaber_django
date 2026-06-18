from django.http import HttpResponse
from django.shortcuts import redirect, render
from turma.forms import TurmaForm
from turma.models import Turma

# Create your views here.
def listar(request):
    lista_turmas = Turma.objects.all()
    contexto = {
        'turmas': lista_turmas
    }
    return render(request, 'turma/listarTurmas.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def cadastrar(request):
    form = TurmaForm(request.POST)
    if form.is_valid():
        dados_turma = form.cleaned_data
        turma = Turma(
            horarioAula = dados_turma['horarioAula'],
            duracaoAula = dados_turma['duracaoAula'],
            dataInicial = dados_turma['dataInicial'],
            codigoTipoAtividade = dados_turma['codigoTipoAtividade'],
            matriculaMonitor = dados_turma['matriculaMonitor'],
            idInstrutor = dados_turma['idInstrutor']
        )

        turma.save()
    return render(request, 'turma/cadastroTurma.html')

def cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def registro_ausencia(request):
    return render(request, 'turma/registroAusencia.html')

def excluir(request, codigoTurma):
    try:
        turma = Turma.objects.get(pk=codigoTurma)
        turma.delete()
    except Turma.DoesNotExist:
        pass
    
    return redirect('turma:listar')

