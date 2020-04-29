from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Producto, Carrito
from orden.models import Orden
from .forms import OrdenForm


# Create your views here.


def datosPedido(request):
    nombre = request.POST.get('nombre') #se guarda en variable lo que se escriba en el input
    apellido = request.POST.get('apellido')#se guarda en variable lo que se escriba en el input
    email = request.POST.get('correo')#se guarda en variable lo que se escriba en el input
    telefono = request.POST.get('telefono')#se guarda en variable lo que se escriba en el input, se convierte el string a numero entero
    
    print(nombre)
     
    orden_form = OrdenForm(request.POST)
    contexto = {'nombre': nombre, 'apellido': apellido,'telefono':telefono, 'email': email}

    if orden_form.is_valid():#si es valido
        carrito = Carrito()
        carrito.save()
        orden_form.save()#guarda en el modelo los datos que se ingresaron
        return redirect('pedidos:lista_productos')

    return render(request, 'pedidos/datos_cliente.html')

def listaProductos(request):
    #iniciar session
    #habia ya una session abierta?
    #orden = Orden.objects.latest('pk')#que guarde en la variable orden_id el id del ultimo pk que se guardo
    #orden_id = orden.id
    #car = Carrito.objects.latest('pk')
    #carrito_id = car.id
    #print(type(orden_id))
    #carrito = Carrito.objects.filter(carritoitem__id = carrito_id)
    
    #print(carrito)
    #nombre = orden.nombre
    #apellido = orden.apellido
    
    print(orden)
    caliente = Producto.objects.filter(categoriaproducto = 1)
    frio = Producto.objects.filter(categoriaproducto = 2)
    sp = Producto.objects.filter(categoriaproducto = 4)
    postre = Producto.objects.filter(categoriaproducto = 3)
    categoria = {'caliente':caliente, 'frio':frio, 'sp':sp, 'postre':postre}

    return render(request, 'pedidos/lista_productos.html', {'categoria':categoria, 'nombre':nombre, 'apellido':apellido, 'carro':carrito})


def carrito(request):
    """
    try:
        orden_id = Orden.objects.latest('pk')
       # the_id = request.session['carrito_id'] #se verifica si la sesion tiene un id
    except:
        orden_id = None #si no tiene id, no se da valor

    if orden_id: #si la variable es TRUE o tiene algun valor u objeto
        carrito = Carrito.objects.get(id = orden_id) #se buscara en el carrito segun el id que tiene the_id
        
        contexto = {'carrito':carrito} #se agregara al contexto el objeto que se rescato con the__id
    else: # si no existe un id, por lo tanto no existen items en el carrito
    """
    mensaje_vacio = "No hay productos, agregalos!" #se deja mensaje en el carrito vacio
    contexto = {'vacio':True, 'mensaje_vacio':mensaje_vacio} #se manda como contexto al renderizar la pagina

    return render(request, 'pedidos/carrito.html', contexto) 

"""
def actualizarCarrito(request, slug):
    try:
        the_id = request.session['carrito_id'] #que verifique si hay una session con el id
    except:# si no hay un id
        nuevo_carrito = Carrito() #se instancia un nuevo carrito
        nuevo_carrito.save() #se guarda el nuevo carrito
        carrito_id = Carrito.objects.latest('pk') 
        the_id = nuevo_carrito.id # se le da el id a la variable the_id

    carrito = Carrito.objects.get(id=the_id) # con el id se rescata el carrito que se creo

    try:
        producto = Producto.objects.get(slug = slug) #busca el producto por el slug que se envia por GET
    except:
        pass

    if not producto in carrito.producto.all():
        carrito.producto.add(producto)
    else:
        print("se agrega producto")

    nuevo_total = 0

    for item in carrito.producto.all();
        nuevo_total += int(item.precio)

    request.session['items_total'] = carrito.producto.count()
    carrito.total = nuevo_total
    carrito.save()

    return """


def datosCliente(request):


    return render(request, 'pedidos/datos_pedido.html')