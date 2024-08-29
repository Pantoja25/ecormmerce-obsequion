from django.shortcuts import render


def login(request):
    template = loader.get_template("formulariologin.html")
    return HttpResponse(template.render())
