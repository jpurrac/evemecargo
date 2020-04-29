from django import forms #from django.forms import ModelForm /tambien puede ser asi
from .models import Contacto #importa el modelo Contacto

class ContactoForm(forms.ModelForm):
    class Meta:#metadatos
        model = Contacto #se dice cual es el modelo que se ocupara en el formulario
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'asunto', 'mensaje']
        #con esto se generará un formulario en nuestra pagina (segun donde lo coloquemos)
