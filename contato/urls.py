from django.urls import path
from . import views 

app_name = 'contato'

urlpatterns = [
     path('cadastro/', views.cadastro, name='cadastro'),
]