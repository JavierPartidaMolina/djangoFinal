from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.index_listado,name="noticiastodo"),
    path('verNoticia/<pk>/', views.index_verArticulo.as_view(),name="verNoticia"),
    path('addNoticia/', views.NoticiaCreateView.as_view(),name="addNoticia"),
    path('updateNoticia/<pk>/', views.NoticiaUpdateView.as_view(),name="updateNoticia"),
    path('delNoticia/<pk>/', views.NoticiaDelete.as_view(),name="delNoticia"),
]