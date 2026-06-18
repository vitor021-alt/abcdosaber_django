from django.urls import path
from . import views 

app_name = 'turma'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('registro_ausencia/', views.registro_ausencia, name='registro_ausencia'),
    path('excluir/<int:codigoTurma>/', views.excluir, name='excluir'),
]