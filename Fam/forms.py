from django import forms

class form_familia(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacimiento = forms.DateField()

class form_ubicaciones(forms.Form):
    ciudad = forms.CharField(max_length=40)
    distrito = forms.CharField(max_length=40)
    Ubigeo = forms.IntegerField()