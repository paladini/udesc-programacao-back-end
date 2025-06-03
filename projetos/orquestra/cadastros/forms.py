from .models import Diretoria
from django import forms

class DiretoriaForm(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields = ['cargo', 'nome', 'contato']

