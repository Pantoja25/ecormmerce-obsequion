from django.urls import path
from.import views

urlpatterns = [
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/adicionar/', views.adicionarItemCarrinho, name='adicionarItemCarrinho'),
    #path('carrinho/remover/<int:id>', views.removerItemCarrinho, name='removerItemCarrinho'),
]
