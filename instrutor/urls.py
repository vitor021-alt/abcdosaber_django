from django.urls import path
from . import views 

app_name = 'instrutor'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigoInstrutor>/', views.excluir, name='excluir'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('carregar_instrutor/<int:codigo>/', views.carregar_instrutor, name='carregar_instrutor'), 
]