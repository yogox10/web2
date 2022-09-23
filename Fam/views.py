from django.shortcuts import render
from Fam.forms import form_familia
from Fam.models import Familia
from django.http import HttpResponse

# Create your views here.

def familia (request): 
    if request.method =="POST":
        familia = Familia (nombre = request.POST['nombre'],edad = request.POST['edad'],nacimiento = request.POST['nacimiento'])
        familia.save()
        return render(request,"familia.html")
    return render ( request , "adicional.html" )

def adicional (request):
    return render (request,"adicional.html" )

def api_familia (request): 
    if request.method == "POST":
        formulario = form_familia(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            familia = Familia(nombre=informacion['nombre'],edad=informacion['edad'],nacimiento=informacion['nacimiento'])
            familia.save()
            return render(request,"api_familia.html")
    else: 
        formulario = form_familia()
    return render (request,"api_familia.html",{"formulario": formulario})


def buscar_pariente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        familias = Familia.objects.filter(nombre__icontains = nombre)
        return render(request,"adicional.html",{"familia":familias})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

