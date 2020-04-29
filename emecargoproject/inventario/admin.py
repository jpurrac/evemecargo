from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.

class ProductoAdmin(admin.ModelAdmin): # de esta forma, en el administrador mostara en forma de lista los registros que se creen
    list_display = ('nombreproducto','precio','categoriaproducto','slug','descripcion','habilitado', 'fechacreacionproducto')
    readonly_fields = ['fechacreacionproducto']
    prepopulated_fields = {"slug": ("nombreproducto",)}
    class Meta:
        model = Producto

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)