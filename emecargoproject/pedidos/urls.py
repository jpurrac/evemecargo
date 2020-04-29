from django.urls import path
from .views import datosPedido, listaProductos, carrito


urlpatterns = [
    path('datos_cliente/', datosPedido, name='datos_cliente'), #que se cree un ID de ORDEN?
    path('lista_productos/', listaProductos, name='lista_productos'),
    path('carrito/', carrito, name='carrito'),

]
    