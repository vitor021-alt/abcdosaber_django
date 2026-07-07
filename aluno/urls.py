from django.urls import path
from . import views 

app_name = 'aluno'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('carregar_aluno/<int:codigo>', views.carregar_aluno, name='carregar_aluno'),
    path('excluir/<int:codigoAluno>/', views.excluir, name='excluir'),
]