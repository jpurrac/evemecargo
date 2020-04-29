from django.db import models
from datetime import datetime #importar fechas
from ckeditor.fields import RichTextField

# Create your models here.
class Asuntos(models.Model):

    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Asunto'
        verbose_name_plural = 'Asuntos'

    def __str__(self):
        return self.asunto # al ser instanciado, se llama con el nombre del ausnto para mostrar

class Contacto(models.Model):
    id = models.AutoField(primary_key=True) #se genera solo
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null = False)
    telefono = models.IntegerField(blank=False, null=False)
    fechacontacto = models.DateField('Fecha Recibo', blank=False, null=False, auto_now_add=True, auto_now=False) #este no se mostrara en el formulario de admin ya que se genera solo
    correo = models.EmailField(blank=False, null=False, unique=False)
    asunto = models.ForeignKey(Asuntos, on_delete=models.CASCADE) #ocupa al modelo Asuntos como clave foranea, para ser mostarados en el formulario
    mensaje = models.TextField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Contacto' # como se mostrara en el admin si hay 1 objeto
        verbose_name_plural = 'Contactos' #como se mostrar en el admin si hay mas de 1 iobjecto

    def __str__(self):
        return self.nombre + " " + self.apellido #al ser instanciado, se moistrara asi /lista en panel de administracion


class Historia(models.Model):
    campo = models.CharField(max_length=10, blank=False, null=False,default="no asignado")
    texto = RichTextField()
    imagen = models.ImageField(upload_to = 'historia/',max_length=255,null=True,blank=True)


    class Meta:
        verbose_name = 'Historia' # como se mostrara en el admin si hay 1 objeto
        verbose_name_plural = 'Historias' #como se mostrar en el admin si hay mas de 1 iobjecto

    def __str__(self):
        return self.campo






