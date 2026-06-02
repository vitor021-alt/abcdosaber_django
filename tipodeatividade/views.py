from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def listar(request):
    return render(request, 'tipodeatividade/listarTiposAtividade.html')

def cadastro(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')