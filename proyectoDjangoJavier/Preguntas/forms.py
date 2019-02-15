from django import forms
from .models import Pregunta,Respuesta

class PreguntaForm(forms.ModelForm):

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs is not None and 'request' in kwargs:
            request = kwargs.pop('request')
        r = super().save(commit=False, *args, **kwargs)

        if 'user' not in kwargs and request is not None:
            r.user = request.user
            r.save()

    class Meta:
        model = Pregunta
        fields = [
            'Pregunta',
        ]

        labels = {
            'Pregunta' : 'Pregunta',
        }

        widgets = {
            'Pregunta': forms.TextInput(attrs={'class':'form-control'}),
        }

class RespuestaForm(forms.ModelForm):

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs is not None and 'request' in kwargs:
            request = kwargs.pop('request')
        r = super().save(commit=False, *args, **kwargs)

        if 'user' not in kwargs and request is not None:
            r.user = request.user
            r.save()

    class Meta:
        model = Respuesta
        fields = [
            'Respuesta',
        ]

        labels = {
            'Respuesta' : 'Respuesta',
        }

        widgets = {
            'Respuesta': forms.TextInput(attrs={'class':'form-control'}),
        }

