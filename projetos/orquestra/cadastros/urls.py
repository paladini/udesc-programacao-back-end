"""
URL configuration for orquestra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('historia/', views.historia, name = 'historia'),
    path('musicos/', views.musicos, name = 'musicos'),
    path('diretoria/', views.diretoria, name = 'diretoria'),
    path('', views.index, name = 'galeria'),
    path('', views.index, name = 'agenda'),
    path('', views.index, name = 'contato'),
    path('cadastrar_diretoria/', views.cadastrar_diretoria, name="cadastrar_diretoria"),
    path('cadastros/', views.home, name='home'),
    path('cadastros/musicos/', views.listar_musicos, name='listar_musicos'),
    path('cadastros/musicos/adicionar/', views.cadastrar_musico, name='adicionar_musico'),
    path('cadastros/musicos/alterar/<int:id>/', views.alterar_musico, name='alterar_musico'),
    path('cadastros/musicos/excluir/<int:id>/', views.excluir_musico, name='excluir_musico'),
]
