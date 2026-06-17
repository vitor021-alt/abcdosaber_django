
from django.http import HttpResponse
from django.shortcuts import redirect, render
from titulo.forms import TituloForm
from titulo.models import Titulo


# Create your views here.
def listar(request):
    lista__titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista__titulos
    }
    return render(request, 'titulo/listarTitulos.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'titulo/cadastroTitulos.html')

def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )

        titulo.save()

    return render(request, 'titulo/cadastroTitulos.html')



def cadastro(request):
    return render(request, 'titulo/cadastroTitulos.html')


def excluir(request, codigoTitulo):
    try:
        titulo = Titulo.objects.get(pk=codigoTitulo)
        titulo.delete()
    except Titulo.DoesNotExist:
        pass
    
    return redirect('titulo:listar')