from django.db import models
from inventario.models import Producto


class CarritoItem(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    total = models.IntegerField(default=0)

    def __str__(self):
        try:
            return str(self.carrito.id)
        except:
            return self.producto.nombreproducto


class Carrito (models.Model):
    carritoitem = models.ManyToManyField(CarritoItem)
    #nombre = models.CharField("Nombre ",max_length=30, blank=False, null=False)
    #apellido = models.CharField("Apellidos ",max_length=30, blank=False, null=False)
    #telefono = models.IntegerField("N° Teléfono ",blank=False, null=False)
    #correo = models.EmailField("Correo: ",blank=False, null=False, unique=False)
    #fechapedido = models.DateField('Fecha Pedido ', blank=False, null=False, auto_now=True)
    #producto = models.ManyToManyField(Producto)
    comentario = models.TextField("Comentario", max_length=100, blank=False, null=False)
    total = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Carrito"

    def __str__(self):
        return "%s" %(self.id)