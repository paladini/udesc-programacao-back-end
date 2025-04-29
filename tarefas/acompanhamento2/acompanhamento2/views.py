from django.shortcuts import render

def index (request):
    return render(request, 'index.html', {'nome' : 'Início'})

def cursos(request):
    return render(request, 'cursos.html', {'nome' : 'Cursos'})

def professores(request):
    return render(request, 'professores.html', {'nome' : 'Professores'})