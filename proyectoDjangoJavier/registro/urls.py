from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('perfiluser/', views.index_perfil,name="perfiluser"),
    path('contactar/', views.contactomail,name="contacto"),
]