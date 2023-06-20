from django.urls import path
from core import views

urlpatterns = [
    path('ativos/', views.lista_ativos, name='lista-ativos'),
    path('ativos/adicionar/', views.adicionar_ativo, name='adicionar-ativo'),
    path('ativos/editar/<int:id>/', views.editar_ativo, name='editar-ativo'),
    path('ativos/excluir/<int:id>/', views.excluir_ativo, name='excluir-ativo'),
]

