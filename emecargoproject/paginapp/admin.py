from django.contrib import admin
from .models import Contacto, Asuntos, Historia

# Register your models here.

#admin.site.register(Contacto) #se registra el modelo dentro del panel de administrador
class ContactoAdmin(admin.ModelAdmin): # de esta forma, en el administrador mostara en forma de lista los registros que se creen
    list_display = ('nombre', 'apellido', 'telefono','fechacontacto', 'correo', 'asunto', 'mensaje') # estos campos se mostraran en la lista

admin.site.register(Contacto, ContactoAdmin) # es necesario colocar el modelo y la clase que se ocupara
admin.site.register(Historia)
admin.site.register(Asuntos)