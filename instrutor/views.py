
from django.http import HttpResponse
from django.shortcuts import redirect, render
from instrutor.forms import InstrutorForm
from instrutor.models import Instrutor

# Create your views here.
def listar(request):
    lista_instrutores = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutores
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def cadastrar(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(
            nome = dados_instrutor['nome'],
            rg = dados_instrutor['rg'],
            dataNascimento = dados_instrutor['dataNascimento'],
            ddd = dados_instrutor['ddd'],
            telefone = dados_instrutor['telefone']
        )
        
        instrutor.save()
    else:
        print(form.errors)

    return render(request, 'instrutor/cadastroInstrutor.html')

def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def excluir(request, codigoInstrutor):
    try:
        instrutor = Instrutor.objects.get(pk=codigoInstrutor)
        instrutor.delete()
    except Instrutor.DoesNotExist:
        pass
    
    return redirect('instrutor:listar')