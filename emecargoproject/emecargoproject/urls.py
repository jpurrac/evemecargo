"""emecargoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from paginapp.views import Home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ #lista con todas las urls que contara el proyecto



    path('admin/',admin.site.urls),
    path('',Home,name='index'), #'', por que solo aparecera la pagina cuando sea /paginapp/ | Llama a la funcion Home y le da nombre a index.html como index
    path('paginapp/',include(('paginapp.urls','paginapp'), namespace="paginapp")), #se incluye en el url principal, el urls de la aplicacion paginapp para que capte sus urls
    path('pedidos/',include(('pedidos.urls','pedidos'), namespace="pedidos")),
    path('inventario/',include(('inventario.urls','inventario'), namespace="inventario")),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)