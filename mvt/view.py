from django.http import HttpResponse
from Fam.models import Familia
from django.template import loader

def home(self):
    return HttpResponse(f"Hola soy Diego Matta")


def parientes(self):    
    familiar= {"nombre":["Diego","Pedro","Mario"],"edad":["70","30","27"],"nacimiento":["1996-07-02","1956-02-02","2002-12-12"]}
    lista = loader.get_template('familia2.html')
    documento = lista.render(familiar)
    return HttpResponse(documento)



