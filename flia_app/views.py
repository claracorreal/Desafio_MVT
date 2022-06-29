from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse
from flia_app.models import Familia

def listar_familia(request):
    context = {}

    context["familiares"] = Familia.objects.all()

    return render(request, "flia_app/familiares.html", context)


