from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = [
            'Titulo',
            'Resumen',
            'Cuerpo',
            'Imagen',
        ]

        labels = {
            'Titulo': 'Titulo',
            'Resumen': 'Resumen',
            'Cuerpo': 'Cuerpo',
            'Imagen': 'Imagen',
        }

        widgets = {
            'Titulo': forms.TextInput(attrs={'class':'form-control'}),
            'Resumen': forms.TextInput(attrs={'class':'form-control'}),
            'Cuerpo':  forms.Textarea(attrs={'class':'form-control'}),
        }
