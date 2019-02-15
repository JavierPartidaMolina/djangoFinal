from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Competiciones, Participaciones
from .forms import CompeticionesForm, ParticipacionesForm
from GestionRopa.models import Tipo
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, UpdateView


def index_listado(request):
    competiciones = Competiciones.objects.all()
    tipo = Tipo.objects.all()
    mensaje = 0 
    return render(request, "competiciones/competiciones_list.html",{'mensaje':mensaje, 'competiciones': competiciones, 'tip': tipo,'logeado' : request.user})

def index_listado_participaciones(request):
    participaciones = Participaciones.objects.filter(User_id=request.user)
    tipo = Tipo.objects.all()
    return render(request, "competiciones/participaciones_user_list.html",{'participaciones': participaciones, 'tip': tipo,'logeado' : request.user})

def index_listado_competiciones(request, id):
    participaciones = Participaciones.objects.filter(Competiciones_id=id)
    tipo = Tipo.objects.all()
    form = ParticipacionesForm
    return render(request, "competiciones/participaciones_competicion_list.html",{'form':form, 'participaciones': participaciones, 'tip': tipo,'logeado' : request.user})

def Asignar_puesto(request, id):
    participacion = Participaciones.objects.get(id=id)
    participacion.posicion=request.POST.get('posicion','')
    participacion.save()
    participaciones=Participaciones.objects.filter(Competiciones=participacion.Competiciones)
    form=ParticipacionesForm
    tipo = Tipo.objects.all()
    return render(request, "competiciones/participaciones_competicion_list.html",{'form':form, 'participaciones': participaciones, 'tip': tipo,'logeado' : request.user})


def crear_participacion(request, id):
    participaciones = Participaciones.objects.filter(Competiciones=id)
    competicion = Competiciones.objects.get(id=id)
    competiciones = Competiciones.objects.all()
    tipo = Tipo.objects.all()
    participa = False
    for i in participaciones:
        if i.User == request.user:
            participa = True
    if participa:
        mensaje = 2 
    else:
        user = request.user
        mensaje = 1 
        participacion = Participaciones(Competiciones = competicion, User = user)
        participacion.save()

    return render(request, "competiciones/competiciones_list.html",{'mensaje': mensaje, 'competiciones': competiciones, 'tip': tipo,'logeado' : request.user})

class CompeticionesCreateView(CreateView):
    model=Competiciones
    form_class = CompeticionesForm
    template_name='competiciones/competicionesform.html'
    success_url= reverse_lazy('competicionestodo')

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tip'] = Tipo.objects.all()
        return context

class CompeticionesDelete(DeleteView):
    model=Competiciones
    template_name='competiciones/competiciones_confirm_delete.html'
    success_url=reverse_lazy('competicionestodo')

class CompeticionesUpdateView(UpdateView):
    model=Competiciones
    form_class = CompeticionesForm
    template_name='competiciones/competicionesform.html'
    success_url= reverse_lazy('competicionestodo')

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.success_url)