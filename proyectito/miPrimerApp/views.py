from django.shortcuts import render
from django.http import HttpResponse
from .models import *

#Create your views here.
def index(request):
    #grupoVar  =  Grupo()
    #grupoVar.save() #Va crear un id = 1 de Grupo
    #estudianteVar  =  Estudiante(numCta=314, nombres="Luis", apellidos="Perez", grupo=5)
    #estudianteVar.save()

    #Obtenemos aquellos estudiantes que están en el grupo con id cinco
    consulta_Estudiante  =  Estudiante.objects.filter()
    print(consulta_Estudiante)
    grupo_idVariable = Grupo.objects.get(id_grupo=1)
    return render(request,'index.html', {'consulta_Estudiante':consulta_Estudiante, 'grupo_idVariable':grupo_idVariable})

def funcionUno(request, grupo_id):
    #Obtenemos aquellos estudiantes que están en el grupo con id cinco
    consulta_Estudiante  =  Estudiante.objects.filter(grupo=1)
    print(consulta_Estudiante)
    return render(request,'Grupo1.html', {'consulta_Estudiante':consulta_Estudiante, 'grupo_id':grupo_id})