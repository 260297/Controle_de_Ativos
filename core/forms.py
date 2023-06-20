from django import forms
from .models import Ativos

class AtivosForm(forms.ModelForm):
    class Meta:
        model = Ativos
        fields = '__all__'  # Inclui todos os campos do modelo no formulário
