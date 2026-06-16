from django.http import HttpResponse
from django.shortcuts import redirect, render
from aluno.models import Aluno 

# Create your views here.
def listar(request):
    lista_alunos = Aluno.objects.all()
    contexto = {
        'alunos': lista_alunos
    }
    return render(request, 'aluno/listarAlunos.html', context=contexto)

def cadastro(request):
    return render(request, 'aluno/cadastroAluno.html')

def excluir(request, codigoAluno):
    try:
        aluno = Aluno.objects.get(matricula=codigoAluno)
        aluno.delete()
    except Aluno.DoesNotExist:
        pass
    
    return redirect('aluno:listar')