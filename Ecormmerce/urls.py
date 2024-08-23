"""
Configuração de URL para o projeto Ecormmerce.

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações, consulte:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
Exemplos:
Função visualizações
1. Adicione uma importação: from my_app import views
2. Adicione uma URL para urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
1. Adicione uma importação: from other_app.views import Home
2. Adicione uma URL para urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
1. Importe a função include(): from django.urls import include, path
2. Adicione uma URL para urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('TelaVenda.urls')),
    path('admin/', admin.site.urls),
]
