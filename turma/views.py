from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def listar(request):
    return render(request, 'turma/listarTurmas.html')

def registro_ausencia(request):
    return render(request, 'turma/registroAusencia.html')
