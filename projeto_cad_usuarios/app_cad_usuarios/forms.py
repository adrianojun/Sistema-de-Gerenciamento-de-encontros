from django import forms
from .models import Usuario, Encontro

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'bairro', 'sexo', 'cidade']
        
class EncontroForm(forms.ModelForm):
    class Meta:
        model = Encontro
        fields = ['usuario', 'data', 'horario']