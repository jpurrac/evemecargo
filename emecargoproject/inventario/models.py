from django.db import models
from datetime import date



class Categoria(models.Model):
    nombrecategoria = models.CharField("Categoría ",max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombrecategoria

class Producto(models.Model):
    nombreproducto = models.CharField("Producto",max_length=30, blank=False, null=False)
    precio = models.IntegerField("Precio")
    categoriaproducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fechacreacionproducto = models.DateField('Fecha Creación de Producto', blank=False, null=False, auto_now_add=False, auto_now=False, default=date.today)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField('Descripción de Producto',max_length=200, blank=False, null=False)
    cantidad = models.IntegerField(default=1)
    habilitado = models.BooleanField("Habilitado / Deshabilitado",default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombreproducto