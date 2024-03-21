from django.shortcuts import render, redirect
from .forms import CreateNewIngreso, ModifyIngreso
from .models import Ingreso
from datetime import datetime
from django.db.models import Count

# Create your views here.


def index(request):

    numeroUltimoIngreso = 0

    if request.method == 'POST':
        ingreso = Ingreso.objects.create(horaIngreso=request.POST['horaIngreso'])
        numeroUltimoIngreso = ingreso.id
        return renderizar(request, numeroUltimoIngreso)

    return renderizar(request)


def renderizar(request, numeroUltimoIngreso=0, isSalidaRegistered=False):

    promedioClientesPorDia()

    return render(request, 'index.html',{
        'formIngreso' : CreateNewIngreso,
        'formSalida' : ModifyIngreso,
        'numeroUltimoIngreso' : numeroUltimoIngreso,
        'isSalidaRegistered' : isSalidaRegistered,
        'promedioDemora' : calcularPromedio(),
        'promedioClientesPorDia' : promedioClientesPorDia()
    })

def salida(request):

    if request.method == "POST":
        ingreso = Ingreso.objects.get(pk=request.POST['nro'])
        numeroUltimoIngreso = 0
        ingreso.horaSalida = request.POST['horaSalida']
        ingreso.save()
        return renderizar(request, numeroUltimoIngreso, isSalidaRegistered=True)

def calcularPromedio():
    tiempoDemorado = 0
    numeroDeIngresos = 0
    ingresos = Ingreso.objects.all()
    for ingreso in ingresos:
        if ingreso.horaSalida != None:
            numeroDeIngresos = numeroDeIngresos + 1
            tiempoDemorado = tiempoDemorado + restarTiemposEnMinutos(ingreso.horaIngreso, ingreso.horaSalida)
            
    if numeroDeIngresos == 0:
        return 0
    promedio = tiempoDemorado / numeroDeIngresos
    
    return int(promedio)


def restarTiemposEnMinutos(horaInicio:datetime.time, horaFin : datetime.time):
    hora_Inicio_Segundos = horaInicio.hour * 3600 + horaInicio.minute * 60 + horaInicio.second
    hora_Fin_Segundos = horaFin.hour * 3600 + horaFin.minute * 60 + horaFin.second
    diferencia = hora_Inicio_Segundos - hora_Fin_Segundos
    if diferencia < 0:
        diferencia = diferencia * -1
    diferenciaEnMinutos = diferencia // 60
    return int(diferenciaEnMinutos)


def promedioClientesPorDia():
    dias = Ingreso.objects.values('fecha').distinct().count()
    ingresos = Ingreso.objects.count()
    if dias == 0:
        return 0
    return ingresos // dias