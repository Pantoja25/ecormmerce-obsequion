from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def TelaVenda(request):
    templete =  loader.get_templet("TelaVenda.html")
    return HttpResponse(templete.render())
