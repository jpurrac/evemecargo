from django.urls import path
from .views import crearContacto, crearHistoria, Galeria, listarContacto, editarContacto, eliminarContacto, menu

urlpatterns = [
    # ..../paginapp/
    #se crea la url para conectar la view
    #1er: como se mostrara la url | 2do: Vista en funciones | 3er: nombre que se le dara a la pagina para ser llamada en otras instancias
    path('historia/', crearHistoria, name='historia'),
    path('galeria/', Galeria, name='galeria'),
    path('contacto/', crearContacto, name='contacto'),
    path('listar_contacto/', listarContacto, name= 'listar_contacto'),
    path('editar_contacto/<int:id>', editarContacto, name='editar_contacto'),
    path('eliminar_contacto/<int:id>', eliminarContacto, name='eliminar_contacto'),
    path('menu', menu, name='menu')
]