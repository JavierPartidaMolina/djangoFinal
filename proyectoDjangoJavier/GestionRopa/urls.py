from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('todo/', views.index_listado,name="ropatodo"),
    url('ropaUser/', views.index_listado_por_usuario,name="ropauser"),
    url('addRopa/', views.RopaCreateView.as_view() ,name='addropa'),
    path('delete/<pk>', views.RopaDelete.as_view(),name="ropadelete"),
    path('updateRopa/<pk>', views.RopaUpdateView.as_view(),name="ropaupdate"),
    path('verArticulo/<int:id>/', views.index_ver_articulo,name="verarticulo"),
    path('formPregunta/<int:id>/', views.crear_pregunta,name="formPregunta"),
    path('formRespuesta/<int:id>/', views.crear_respuesta,name="formRespuesta"),
    path('deleteresp/<pk>', views.RespuestaDelete.as_view(),name="respdelete"),
    path('preguntaDelete/<pk>', views.preguntaDelete.as_view(),name="preguntaDelete"),
    path('informacion/', views.informacion.as_view(),name="info"),
    path('lisTipos/', views.tipo_list.as_view(),name="tipos"),
    path('addTipo/', views.TipoCreateView.as_view() ,name='añadirtipo'),
    path('deletetipo/<pk>', views.TipoDelete.as_view(),name="deltipo"),
    path('tipoupdate/<pk>', views.TipoUpdateView.as_view(),name='tipoupdate'),
    
    path('lisTejido/', views.Tejido_list.as_view(),name="tejidos"),
    path('addTejido/', views.TejidoCreateView.as_view() ,name='añadirtejido'),
    path('deleteTejido/<pk>', views.TejidoDelete.as_view(),name="deltejido"),
    path('Tejidoupdate/<pk>', views.TejidoUpdateView.as_view(),name='tejidoupdate'),
]

