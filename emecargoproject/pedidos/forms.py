from django import forms #from django.forms import ModelForm /tambien puede ser asi
from orden.models import  Orden#importa el modelo Contacto

class OrdenForm(forms.ModelForm):
    class Meta:#metadatos
        model = Orden #se dice cual es el modelo que se ocupara en el formulario
        fields = ['nombre', 'apellido', 'telefono', 'correo']