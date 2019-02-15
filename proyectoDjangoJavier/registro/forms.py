from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import perfil

class FormularioContacto(forms.Form):
    correo = forms.EmailField()
    mensaje = forms.CharField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': 'compact',
        }
    ))
    


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}), max_length=32, help_text='First name')
    last_name=forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}), max_length=32, help_text='Last name')
    email=forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2=forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita contraseña'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)