from django.http import HttpResponse
from django.shortcuts import render
from tipodeatividade.models import Tipodeatividade



# Create your views here.
def listar(request):
    lista_tipos_atividade = Tipodeatividade.objects.all()
    contexto = {
        'tipos_atividade': lista_tipos_atividade
    }
    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

def cadastro(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')