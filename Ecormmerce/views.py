from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def login_html(request):
        template = loader.get_template("login.html")
        return HttpResponse(template.render(request=request))