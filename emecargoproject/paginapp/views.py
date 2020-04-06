from django.shortcuts import render

# Create your views here.
def Home(request): #se comunicara con URLS
    return render(request,'index.html')

def crearContacto(request):
    if request.method == 'POST': #si el request que se manda por la pagina es POST