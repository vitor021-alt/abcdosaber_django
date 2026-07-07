from django.urls import path
from . import views 

app_name = 'tipodeatividade'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigo>', views.excluir, name='excluir'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('carregar_tipodeatividade/<int:codigo>', views.carregar_tipodeatividade, name='carregar_tipodeatividade'),
]