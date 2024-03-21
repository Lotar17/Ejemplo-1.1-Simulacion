from django.db import models

# Create your models here.


class Ingreso(models.Model):
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    horaIngreso = models.TimeField(auto_now=False, auto_now_add=False)
    horaSalida = models.TimeField(auto_now=False, auto_now_add=False,null=True)