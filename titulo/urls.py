from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('futebol/', views.futebol),
    path('show_view/', views.show_view,),
    path('listar_exemplo/', views.listar_exemplo,),
    path('abc/', views.abc,),
]