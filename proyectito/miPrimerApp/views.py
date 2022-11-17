from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
#se agregan estas linas
from .form import *
from django.contrib.auth import authenticate, login

from datetime import datetime

#Create your views here.
@login_required
def index(request):
    #grupoVar  =  Grupo()
    #grupoVar.save() #Va crear un id = 1 de Grupo
    #estudianteVar  =  Estudiante(numCta=314, nombres="Luis", apellidos="Perez", grupo=5)
    #estudianteVar.save()

    #Obtenemos aquellos estudiantes que están en el grupo con id cinco
    consulta_Estudiante  =  Estudiante.objects.filter()
    print(consulta_Estudiante)
    grupo_idVariable = Grupo.objects.get(id_grupo=1)
    grupo_idVariableDos = Grupo.objects.get(id_grupo=2)
    hoy = datetime.now()
    print(hoy.weekday())
    return render(request,'index.html', {'consulta_Estudiante':consulta_Estudiante, 'grupo_idVariable':grupo_idVariable, 'grupo_idVariableDos':grupo_idVariableDos})
@login_required
def funcionUno(request, grupo_id):
    #Obtenemos aquellos estudiantes que están en el grupo con id cinco
    consulta_Estudiante  =  Estudiante.objects.filter(grupo=2)
    grupo_idVariable = Grupo.objects.get(id_grupo=1)
    print(consulta_Estudiante)
    hoy = datetime.now()
    print(hoy.weekday())

    if hoy.weekday() == 3: 
        #return HttpResponse('Hoy es jueves') 
        return redirect('miPrimerApp:DOS', grupo_id=grupo_idVariable) 
    return render(request,'Grupo1.html', {'consulta_Estudiante':consulta_Estudiante, 'grupo_id':grupo_id})
@login_required
def funcionDos(request, grupo_id):
    #Obtenemos aquellos estudiantes que están en el grupo con id cinco
    consulta_Estudiante  =  Estudiante.objects.filter(grupo=2)
    print(consulta_Estudiante)
    return render(request,'Grupo2.html', {'consulta_Estudiante':consulta_Estudiante, 'grupo_id':grupo_id})

def registro(request):
	data = {
		'form': CustomUserCreationForm()
	}
	if request.method == "POST":
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			usuario = formulario.save()
			usuario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			login(request,user)
			return redirect(to="miPrimerApp:index")
		data["form"] = formulario
	return render(request,'registration/registration.html', data)

def home(request):

    return render(request,'home.html')