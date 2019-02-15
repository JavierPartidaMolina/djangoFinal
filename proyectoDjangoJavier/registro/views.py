#from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from .models import perfil
from django.core.mail import EmailMessage
from django.template import RequestContext
from .forms import SignUpForm, FormularioContacto


class SignUpView(CreateView):
    model = perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login')

def index_perfil(request):
    return render(request,"registro/perfil.html", {'logeado' : request.user})

def contactomail(request):

    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            asunto = "Mensaje desde QCDC"
            mensaje = formulario.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=['javier.partida.molina@gmail.com'])
            mail.send()
            correcto = "Mensaje enviado correctamente"
            resp = 0
            return render(request,"registro/perfil.html", {'logeado' : request.user , 'mensaje' : correcto,'resp' : resp})
        else:
            formulario = FormularioContacto()
            resp = 1
            return render(request,'registro/contactar.html', {'form' : formulario , 'resp' : resp})
    else:
        formulario = FormularioContacto()
        resp = 0
        return render(request,'registro/contactar.html', {'form' : formulario,'resp' : resp})





 
