from django.db import models
from pedidos.models import Carrito 

# Create your models here.
class Orden(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    nombre = models.CharField("Nombre ",max_length=30, blank=False, null=False)
    apellido = models.CharField("Apellidos ",max_length=30, blank=False, null=False)
    telefono = models.IntegerField("N° Teléfono ",blank=False, null=False)
    correo = models.EmailField("Correo: ",blank=False, null=False, unique=False)
    fechapedido = models.DateField('Fecha Pedido ', blank=False, null=False, auto_now=True)
    

    class Meta:
        verbose_name = "Orden"

    def __str__(self):
        return "%s" %(self.id)