from .models import Diretoria, Musico
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DiretoriaForm(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields = ['cargo', 'nome', 'contato']

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = '__all__'

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']