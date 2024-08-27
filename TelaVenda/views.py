from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Venda


def pagina1(request):
    template = loader.get_template("pagina1.html")
    return HttpResponse(template.render())

def Venda(request):
    template = loader.get_template("Venda.html")
    return HttpResponse(template.render())


def formulario(request):
    template = loader.get_template("formulario.html")
    return formulario(template.render())

def VendaConcluida(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    return render(request, 'vendas/VendaConcluida.html', {'venda': venda})