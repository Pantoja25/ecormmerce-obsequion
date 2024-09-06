from django.urls import path
from.import views

urlpatterns = [
    path('', views.pagina1, name="Pagina1"),
    path('Venda/', views.Venda, name="Venda"),
    path('formulario/', views.formulario, name="formulario"),
    path('VendaConcluida/', views.VendaConcluida, name="VendaConcluida"),
    
]
