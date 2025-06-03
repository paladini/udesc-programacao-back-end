from .models import Diretoria, Musico
from django import forms

class DiretoriaForm(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields = ['cargo', 'nome', 'contato']

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = '__all__'