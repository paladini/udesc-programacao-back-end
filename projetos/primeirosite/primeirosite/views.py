from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    """
    View function for the home page of the site.
    """
    return HttpResponse("Olá, mundo! Pela enésima vez.")

def qual_dia(request):
    dia_formatado = datetime.datetime.now().strftime('%d/%m/%Y')
    context = {'nome' : 'Seu Nome', 'hoje' : dia_formatado}
    return render(request, "qual_dia.html", context)