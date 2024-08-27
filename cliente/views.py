from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def novo_cliente(request):
    template = loader.get_template("novo_cliente.html")
    return HttpResponse(template.render())

def tela_de_sucesso(request):
    template = loader.get_template("tela_de_sucesso.html")
    

    contexto = {
        "nome": request.GET.get("nome"),
        "cpf": request.GET.get("cpf"),
        "telefone": request.GET.get("telefone"),
        "email": request.GET.get("email"),
        "endereco": request.GET.get("endereco"),
    }
    return HttpResponse(template.render(contexto, request))

