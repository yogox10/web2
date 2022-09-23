from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()


class ubicaciones(models.Model):
    ciudad = models.CharField(max_length=40)
    distrito = models.CharField(max_length=40)
    Ubigeo = models.IntegerField()


class profesiones(models.Model):
    carrera = models.CharField(max_length=40)
    fecha_egreso = models.DateField()
    universidad = models.CharField(max_length=40)




