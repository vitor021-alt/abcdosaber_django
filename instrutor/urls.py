from django.urls import path
from . import views 

app_name = 'instrutor'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/<int:codigoInstrutor>/', views.excluir, name='excluir'),
]