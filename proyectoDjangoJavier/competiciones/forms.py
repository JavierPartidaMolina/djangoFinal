from django import forms
from .models import Competiciones, Participaciones

class CompeticionesForm(forms.ModelForm):

    class Meta:
        model = Competiciones
        fields = [
            'Nombre',
            'Lugar',
            'Descripcion',
            'Fecha',
        ]

        labels = {
            'Nombre': 'Nombre',
            'Lugar': 'Lugar',
            'Descripcion': 'Descripcion',
            'Fecha': 'Fecha',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Lugar': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion':  forms.Textarea(attrs={'class':'form-control'}),
            'Fecha': forms.DateInput(attrs={'class':'form-control'}),
        }

class ParticipacionesForm(forms.ModelForm):

    class Meta:
        model = Participaciones
        fields = [
            'posicion',
        ]

        widgets = {
            'posicion': forms.TextInput(attrs={'class':'form-control'}),
        }