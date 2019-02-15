from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Noticia
from .forms import NoticiaForm
from GestionRopa.models import Tipo
from django.urls import reverse, reverse_lazy

# Create your views here.
def index_listado(request):
    noticias = Noticia.objects.all()
    tipo = Tipo.objects.all()
    return render(request, "noticias_list.html",{'noticias': noticias, 'tip': tipo,'logeado' : request.user})

class index_verArticulo(DetailView):
    model=Noticia
    template_name = 'verNoticia.html'
    slug_field = 'noticia'

class NoticiaDelete(DeleteView):
    model=Noticia
    template_name='noticia_confirm_delete.html'
    success_url=reverse_lazy('noticiastodo')

class NoticiaCreateView(CreateView):
    model=Noticia
    form_class = NoticiaForm
    template_name='noticiaform.html'
    success_url= reverse_lazy('noticiastodo')

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)

class NoticiaUpdateView(UpdateView):
    model=Noticia
    form_class = NoticiaForm
    template_name='noticiaform.html'
    success_url= reverse_lazy('noticiastodo')

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)
