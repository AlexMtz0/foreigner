from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Casas
from django.http import Http404
from .forms import CrearCasa

# Create your views here.

def index(response):
    return render(response, 'main/index.html')

# Función para consultar una casa, pasa por parámetro de ID
def mostrar_casa(request, casa_id):
    Casa = Casas.objects.get(pk=casa_id) #Casa es igual al ID solicitado
    if Casa is not None: #Si no existe id, entonces se muestra error
        return render(request, 'main/casa.html', {'casa':Casa})
    else:
        raise Http404('Movie does not exist')

#Función para crear una casa
def crear_casa(response):
    if response.method == "POST": #Si la acción es POST
        form = CrearCasa(response.POST) #form es igual a toda la información enviada en el método POST
        if form.is_valid():
            #Aquí se guarda cada uno de los campos del formulario en variables
            cn = form.cleaned_data["casa_nombre"] 
            cd = form.cleaned_data["casa_descripcion"]
            cdi = form.cleaned_data["casa_direccion"]
            cdh = form.cleaned_data["casa_habitantes"]
            cc = form.cleaned_data["casa_cuartos"]
            ca = form.cleaned_data["casa_amueblada"]
            ccon = form.cleaned_data["casa_contacto"]
            cr = form.cleaned_data["casa_responsable"]
            #Obj es igual a los campos del modelo de casa, con las variables anteriores.
            obj = Casas(casa_nombre=cn, casa_descripcion=cd, casa_direccion=cdi, casa_habitantes=cdh, casa_cuartos=cc, casa_amueblada=ca, casa_contacto=ccon,casa_responsable=cr)
            obj.save() #Guardamos obj, o sea esta información se pasará a la base de datos
            response.user.casaspropias.add(obj)
    else:
        form = CrearCasa()
    return render(response, "main/crear.html", {"form":form})

def disponibles_casa(request):
    casas = Casas.objects.all()
    return render(request,"main/disponibles.html", {"casas":casas})

def propiedades_casa(request):
    return render(request, "main/propiedades.html", {})
