
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def listar(request):
    return render(request, 'instrutor/listarInstrutores.html')

def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')