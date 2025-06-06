from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Prefetch
from .models import Diretoria, Naipe, Musico
from .forms import DiretoriaForm, MusicoForm, UsuarioForm

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages

def index (request):
    return render(request, 'index.html', {'nome' : 'Fazendo Música'})

def historia(request):
    return render(request, 'historia.html', {'nome' : 'Fazendo Música'})

def musicos(request):
    # naipes = Naipe.objects.prefetch_related('musico_set').all().order_by('nome')
    musicos_ordenados = Musico.objects.order_by('nome')
    naipes = Naipe.objects.prefetch_related(Prefetch('musico_set', queryset = musicos_ordenados)).order_by('nome')
    return render(request, 'musicos.html', {'nome' : 'Fazendo Música', 'naipes' : naipes})

def diretoria(request):

    #componentes = [{'cargo' : 'Presidente', 'nome' : 'Presidente da Orquestra', 'contato' : 'pres@orquestra.com'},
    #               {'cargo' : 'Tesoureiro', 'nome' : 'Tesoureiro da Orquestra', 'contato' : 'tesou@orquestra.com'},
    #               {'cargo' : 'Secretario', 'nome' : 'Secretario da Orquestra', 'contato' : 'sec@orquestra.com'},
    #               ]
    componentes = Diretoria.objects.all()

    return render(request, 'diretoria.html', {'nome' : 'Fazendo Música', 'componentes' : componentes})

def cadastrar_diretoria(request):
    if request.method == 'POST':
        form = DiretoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diretoria')
    else:
        form = DiretoriaForm()

    return render(request, 'cadastrar_diretoria.html', {'form': form })

# @permission_required('cadastro.view_musico', raise_exception=True)
def listar_musicos(request):
    musicos = Musico.objects.all()
    return render(request, 'cadastros/listar_musicos.html', {'musicos': musicos})

@permission_required('cadastro.add_musico', raise_exception=True)
def cadastrar_musico(request):
    if request.method == 'POST':
        form = MusicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_musicos')
    else:
        form = MusicoForm()
    return render(request, 'cadastros/forms_musicos.html', {'form': form})

@permission_required('cadastro.change_musico', raise_exception=True)
def alterar_musico(request, id):
    musico = get_object_or_404(Musico, codigo = id)
    if request.method == 'POST':
        form = MusicoForm(request.POST, request.FILES, instance=musico)
        if form.is_valid():
            form.save()
            return redirect('listar_musicos')
    else:
        form = MusicoForm(instance=musico)
    return render(request, 'cadastros/forms_musicos.html', {'form': form})

# @permission_required('cadastros.delete', raise_exception=True)
@login_required
def excluir_musico(request, id):

    if not request.user.has_perm('cadastros.delete_musico'):
        messages.error(request, 'Você não tem acesso à exclusão de músicos!')
        return redirect('listar_musicos')
    else:
        musico = get_object_or_404(Musico, codigo = id)
        musico.delete()
        return redirect('listar_musicos')

def home(request):
    return render(request, 'cadastros/home.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo = Group.objects.get(name = 'Cadastros')
            user.groups.add(grupo)
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request, 'cadastros/forms_usuario.html', {'form': form})