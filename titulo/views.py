
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_view(request):
    return HttpResponse('<p>Minha View do App titulo</p>')

def listar_exemplo(request):
    pagina = 'Ola, Mundo!'
    return HttpResponse(pagina)

def abc(request):
    pagina = 'ABC'
    return HttpResponse(pagina)

def index(request):
    return render(request, 'index.html')

def futebol(request):
    return render(request, 'futebol.html')