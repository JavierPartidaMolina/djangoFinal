from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.index_listado,name="competicionestodo"),
    path('addParticipacion/<int:id>', views.crear_participacion,name="addParticipacion"),
    path('addCompeticion/', views.CompeticionesCreateView.as_view(),name="addCompeticion"),
    path('updateNoticia/<pk>/', views.CompeticionesUpdateView.as_view(),name="updateCompeticion"),
    path('delCompeticion/<pk>/', views.CompeticionesDelete.as_view(),name="delCompeticion"),
    path('participacionesUser/', views.index_listado_participaciones,name="participacionesUser"),
    path('participacionesCom/<int:id>', views.index_listado_competiciones,name="participacionesCom"),
    path('editParticipacion/<int:id>/', views.Asignar_puesto,name="editParticipacion"),
]