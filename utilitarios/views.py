from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def neymar(request):
    pagina = 'ABC'
    return HttpResponse(pagina)


def index(request):
    return render(request, 'index.html')

