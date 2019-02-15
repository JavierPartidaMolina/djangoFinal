"""proyectoDjangoJavier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from GestionRopa.views import index_listado, index_listado_categoria, index_listado_por_usuario,index_ver_articulo
from django.conf import settings
from django.contrib.auth.views import LoginView
from registro.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ropa/', include('GestionRopa.urls')),
    path('noticias/', include('noticias.urls')),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('',LoginView.as_view(template_name='registro/login.html')),
    path('/',LoginView.as_view(template_name='registro/login.html') , name='login'),
    path('categorias/<int:id>',index_listado_categoria , name='categoria'),
    path('perfil/',include('registro.urls')),
    path('competiciones/',include('competiciones.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)