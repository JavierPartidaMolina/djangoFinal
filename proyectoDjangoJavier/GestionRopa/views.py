from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, UpdateView
from .models import Ropa, Tipo, Tejido
from .forms import  RopaForm, TipoForm, TejidoForm
from django.urls import reverse, reverse_lazy
from Preguntas.models import Pregunta, Respuesta
from Preguntas.forms import PreguntaForm, RespuestaForm
from Preguntas.views import crear
from GestionRopa.models import Ropa

# Create your views here.
def index_listado(request):
    ropa = Ropa.objects.all()
    tipo = Tipo.objects.all()
    return render(request, "ropa/ropa_list.html",{'ropa': ropa, 'tip': tipo,'logeado' : request.user})

def index_listado_categoria(request, id):
    ropa = Ropa.objects.filter(Tipo=id)
    tipo = Tipo.objects.all()
    return render(request, "ropa/ropa_list.html",{'ropa': ropa, 'tip': tipo})

def index_listado_por_usuario(request):
    ropa = Ropa.objects.filter(user=request.user)
    tipo = Tipo.objects.all()
    return render(request, "ropa/ropa_list.html",{'ropa': ropa, 'tip': tipo,'logeado' : request.user})

def crear_respuesta(request, id):
    if request.method == 'POST':
        resp = RespuestaForm(data=request.POST)
        if resp.is_valid():
            respuesta = request.POST.get('Respuesta','')
            pregunta = Pregunta.objects.get(id=id)
            user = request.user
            respues = Respuesta(Pregunta = pregunta, user = user, Respuesta = respuesta)
            respues.save()
            ropa = Ropa.objects.get(id=pregunta.Ropa.id)
            tipo = Tipo.objects.all()
            preguntas = Pregunta.objects.filter(Ropa = ropa)
            respuestas = []
            pregunta_form= PreguntaForm
            for i in preguntas:
                respuestas += Respuesta.objects.filter(Pregunta_id = i.id)
            return render(request, "ropa/verArticulo.html",{'RespuestaForm' : RespuestaForm,'formPregunta' : pregunta_form,'respuestas' : respuestas,'preguntas' : preguntas, 'ropa': ropa, 'tip': tipo,'logeado' : request.user}) 

def crear_pregunta(request, id):
    if request.method == 'POST':
        preg = PreguntaForm(data=request.POST)
        if preg.is_valid():
            pregunta = request.POST.get('Pregunta','')
            ropa = Ropa.objects.get(id=id)
            user = request.user
            pregun = Pregunta(Pregunta = pregunta, user = user, Ropa = ropa)
            print(pregun)
            pregun.save()
            ropa = Ropa.objects.get(id=id)
            tipo = Tipo.objects.all()
            preguntas = Pregunta.objects.filter(Ropa = ropa)
            respuestas = []
            pregunta_form= PreguntaForm
            for i in preguntas:
                respuestas += Respuesta.objects.filter(Pregunta_id = i.id)
            return render(request, "ropa/verArticulo.html",{'RespuestaForm' : RespuestaForm,'formPregunta' : pregunta_form,'respuestas' : respuestas,'preguntas' : preguntas, 'ropa': ropa, 'tip': tipo,'logeado' : request.user})             

def index_ver_articulo(request,id):
    ropa = Ropa.objects.get(id=id)
    tipo = Tipo.objects.all()
    preguntas = Pregunta.objects.filter(Ropa = ropa)
    respuestas = []
    pregunta_form= PreguntaForm
    for i in preguntas:
        respuestas += Respuesta.objects.filter(Pregunta_id = i.id)
    return render(request, "ropa/verArticulo.html",{'RespuestaForm' : RespuestaForm, 'formPregunta' : pregunta_form,'respuestas' : respuestas,'preguntas' : preguntas, 'ropa': ropa, 'tip': tipo,'logeado' : request.user}) 

class RopaCreateView(CreateView):
    model=Ropa
    form_class = RopaForm
    template_name='ropa/ropaform.html'
    success_url= reverse_lazy('ropauser')

    def form_valid(self, form):
        self.object = form.save(request=self.request)
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tip'] = Tipo.objects.all()
        return context

class RopaUpdateView(UpdateView):
    model=Ropa
    form_class = RopaForm
    template_name='ropa/ropaform.html'
    success_url= reverse_lazy('ropauser')

    def form_valid(self, form):
        self.object = form.save(request=self.request)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class RopaDelete(DeleteView):
    model=Ropa
    template_name='ropa/ropa_confirm_delete.html'
    success_url=reverse_lazy('ropatodo')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class RespuestaDelete(DeleteView):
    model=Respuesta
    template_name='ropa/respuesta_confirm_delete.html'
    success_url=reverse_lazy('ropatodo')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class preguntaDelete(DeleteView):
    model=Pregunta
    template_name='ropa/pregunta_confirm_delete.html'
    success_url=reverse_lazy('ropatodo')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class informacion(TemplateView):
    template_name = 'ropa/informacion.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class tipo_list(ListView):
    model=Tipo
    template_name = 'ropa/listTipos.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class TipoDelete(DeleteView):
    model=Tipo
    template_name='ropa/tipo_confirm_delete.html'
    success_url=reverse_lazy('tipos')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class TipoCreateView(CreateView):
    model=Tipo
    form_class = TipoForm
    template_name='ropa/tipoform.html'
    success_url= reverse_lazy('tipos')

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class TipoUpdateView(UpdateView):
    model=Tipo
    form_class = TipoForm
    template_name='ropa/tipoform.html'
    success_url= reverse_lazy('tipos')

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class Tejido_list(ListView):
    model=Tejido
    template_name = 'ropa/listTejidos.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class TejidoDelete(DeleteView):
    model=Tejido
    template_name='ropa/tejido_confirm_delete.html'
    success_url=reverse_lazy('tejidos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class TejidoCreateView(CreateView):
    model=Tejido
    form_class = TejidoForm
    template_name='ropa/tejidoform.html'
    success_url= reverse_lazy('tejidos')

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

class TejidoUpdateView(UpdateView):
    model=Tejido
    form_class = TejidoForm
    template_name='ropa/tejidoform.html'
    success_url= reverse_lazy('tejidos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tip'] = Tipo.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)