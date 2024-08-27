from django.urls import path
from . import views
urlpatterns = [
    path('tela_de_sucesso/', views.tela_de_sucesso, name="tela_de_sucesso"),
    path('novo_cliente/', views.novo_cliente, name="novo_cliente"),
    
]
