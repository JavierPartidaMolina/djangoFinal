from django import forms
from .models import Ropa, Tejido, Tipo

class RopaForm(forms.ModelForm):

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs is not None and 'request' in kwargs:
            request = kwargs.pop('request')
        r = super().save(commit=False, *args, **kwargs)

        if 'user' not in kwargs and request is not None:
            r.user = request.user
            r.save()

    class Meta:
        model = Ropa
        fields = [
            'Nombre',
            'Precio',
            'Talla',
            'Imagen',
            'Tipo',
            'Tejido',
            'Tienda'
        ]

        labels = {
            'Nombre': 'Nombre',
            'Precio': 'Precio',
            'Talla': 'Talla',
            'Imagen': 'Imagen',
            'Tipo': 'Tipo',
            'Tejido': 'Tejido',
            'Tienda' : 'Tienda'
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Precio': forms.NumberInput(attrs={'class':'form-control'}),
            'Talla':  forms.TextInput(attrs={'class':'form-control'}),
            'Tipo': forms.Select(attrs={'class':'form-control'}),
            'Tejido': forms.Select(attrs={'class':'form-control'}),
            'Tienda': forms.TextInput(attrs={'class':'form-control'}),
        }


class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = [
            'Nombre'
        ]

        labels = {
            'Nombre': 'Nombre'
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'})
        }

class TejidoForm(forms.ModelForm):

    class Meta:
        model = Tejido
        fields = [
            'Nombre'
        ]

        labels = {
            'Nombre': 'Nombre'
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'})
        }