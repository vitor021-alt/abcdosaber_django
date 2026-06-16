
from django.http import HttpResponse
from django.shortcuts import redirect, render
from instrutor.models import Instrutor

# Create your views here.
def listar(request):
    lista_instrutores = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutores
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def excluir(request, codigoInstrutor):
    try:
        instrutor = Instrutor.objects.get(pk=codigoInstrutor)
        instrutor.delete()
    except Instrutor.DoesNotExist:
        pass
    
    return redirect('instrutor:listar')