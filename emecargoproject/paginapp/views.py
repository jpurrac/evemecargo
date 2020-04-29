from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import ContactoForm
from .models import Contacto, Asuntos, Historia
from email.mime.image import MIMEImage
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

# Create your views here.
def Home(request): #se comunicara con URLS
    return render(request,'index.html')

def crearHistoria(request):
    text1 = Historia.objects.get(pk=1)
    text2 = Historia.objects.get(pk=2)
    text3 = Historia.objects.get(pk=3)

    contexto = {'text1':text1, 'text2':text2, 'text3':text3}
    return render(request,'paginapp/historia.html', contexto)

def Galeria(request):
    return render(request,'paginapp/galeria.html')

def crearContacto(request):

    spinner = Asuntos.objects.all() #se llama Modelo Asunto para sacarlos todos, y poder meterlos a un 'Spinner'. Se manda como parte del contexcto
    
    if request.method == 'POST': #si el request que se manda por la pagina es POST


        nombre = request.POST.get('nombre') #se guarda en variable lo que se escriba en el input
        apellido = request.POST.get('apellido')#se guarda en variable lo que se escriba en el input
        ecorreo = request.POST.get('correo')#se guarda en variable lo que se escriba en el input
        telefono = int(request.POST.get('telefono'))#se guarda en variable lo que se escriba en el input, se convierte el string a numero entero
        asunto = request.POST.get('asunto')#se guarda en variable lo que se escriba en el input
        mensaje = request.POST.get('mensaje')#se guarda en variable lo que se escriba en el input

        print(nombre)
        print(apellido)
       
        
        asun = Asuntos.objects.get(id=asunto) #se trae al ASUNTO que coincida con el id que se trae del input, para darselo al asunto del correo y pueda aparecer el nombre del asunto

        contexto = {'nombre': nombre, 'apellido': apellido,'telefono':telefono, 'ecorreo': ecorreo, 'asunto':asun, 'mensaje':mensaje} #se crea un contexto para mandar los datos del input hacia el formulario que se enviara a correo
        img_path = '/static/img/logo3.png'
        #-- FORMATO QUE LLEGA AL CORREO DEL FARO *----
        with open(settings.BASE_DIR + "/templates/paginapp/email.txt") as txt:
            email = txt.read()
        correo = EmailMultiAlternatives(subject='Formulario de Contacto Restorán Faro Belén : '+asun.asunto,body=email,from_email=settings.EMAIL_HOST_USER, to=['farobelenccp@gmail.com'])
        #-- FORMATO CORREO CLIENTE
        with open(settings.BASE_DIR + "/templates/paginapp/emailcliente.txt") as ctxt:
            cemail = ctxt.read()
        ccorreo = EmailMultiAlternatives(subject='Formulario de Contacto Restorán Faro Belén : '+asun.asunto,body=cemail,from_email=settings.EMAIL_HOST_USER, to=[ecorreo])

        with open(settings.BASE_DIR + "/media/historia/logo3.png", mode='rb') as img:
            image = MIMEImage(img.read())
            
        correo_template_cliente = get_template('paginapp/emailcliente.html').render(contexto)
        correo_template = get_template('paginapp/email.html').render(contexto) #se llama el template del correo, y se renderiza el contexto de las variables que se guardaron en el input
        #se coloca la configuracion del correo, asunto del correo, contenido del correo, quien manda el correo, para quien es el correo,
        
        ccorreo.attach_alternative(correo_template_cliente,"text/html")
        ccorreo.attach(image)
       
        correo.attach_alternative(correo_template,"text/html")

        ccorreo.send()
        correo.send() #se manda el correo con los datos
      
        messages.success(request, "Su mensaje ya fue recepcionado. Muchas Gracias por comunicarte con nosotros")
        contacto_form = ContactoForm(request.POST) #instancia de form que guardara los datos enviados
        if contacto_form.is_valid():#si es valido
            
            contacto_form.save()#guarda en el modelo los datos que se ingresaron
            
            return redirect('index') #una ves guardado, se redirecciona al index

    else:
        contacto_form = ContactoForm() #GET/ cuando entre a la pagina lo hace con GET, por lo tanto se mostara el formulario vacio para ser llenado

    return render(request, 'paginapp/contacto.html',{'contacto_form': contacto_form, 'spinner':spinner})
    #se devuelve con un return, la renderizacion de la pagina
    #como 1er paratmetro es el request, 2do: la dirreccion de la pagina que se devolvera, 3ro: se pasa el contexto a la pagina

def listarContacto(request):
    contactos = Contacto.objects.all()
    print (contactos)
    return render(request, 'paginapp/listar_contactos.html', {'contacto':contactos})
    
def editarContacto(request,id):#recibe por url el id del objeto que se editara
    #El try/catch se ocupa para el manejo de errores o excepciones, en este caso para cuando se inserte o se busque un id que no existe
    contacto_form = None
    error = None
    try:
        contacto = Contacto.objects.get(id = id) #Query, se buscara el objeto que tenga por ID el ID que se da por método, lo cual trae la infromacion a pantalla
        if request.method=='GET': #si el metodo es un GET
            contacto_form = ContactoForm(instance=contacto) #se guarda en el form, una instancia de contacto
            print (contacto_form)
        else: #despues del GET, actua el POST, cuando se ha modificado algun campo, ahora se debe guardar, por lo tanto se genera un metodo POST que envia la info
            contacto_form = ContactoForm(request.POST, instance=contacto) #se guarda la nueva info en la variable
            if contacto_form.is_valid(): #si el formulario es valido,
                contacto_form.save() #el fomrulario se guardara en el modelo
            return redirect ('index') #cuando se guarda la info, se redirige a la pagina index
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'paginapp/contacto.html',{'contacto_form': contacto_form, 'error':error})


#para eliminar, tambien se puede dejar como "estado" deshabilitado.
#para eso, se debe modificar el modelo y agregar un campo de estado (BOOLEAN) ELIMINACION LOGICA Y 
####### ELIMINACION DIRECTA ######
def eliminarContacto(request,id):
    contacto = Contacto.objects.get(id = id) #Query, se buscara el objeto que tenga por ID el ID que se da por método, lo cual trae la infromacion a pantalla
    if request.method=='POST': #si el metodo es un GET
        contacto.delete()
        return redirect('paginapp:listar_contacto')
    return render(request, 'paginapp/eliminar_contacto.html',{'contacto': contacto})


def menu(request):
    return render(request, 'paginapp/menu.html')
