from django.http import HttpResponse
from django.shortcuts import redirect, render
from turma.models import Turma

# Create your views here.
def cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def listar(request):
    lista_turmas = Turma.objects.all()
    contexto = {
        'turmas': lista_turmas
    }
    return render(request, 'turma/listarTurmas.html', context=contexto)

def registro_ausencia(request):
    return render(request, 'turma/registroAusencia.html')

def excluir(request, codigoTurma):
    try:
        turma = Turma.objects.get(pk=codigoTurma)
        turma.delete()
    except Turma.DoesNotExist:
        pass
    
    return redirect('turma:listar')

