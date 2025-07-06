from django.shortcuts import render, redirect
from Modelo.ModeloFarmacia.Farmacias.models import Farmacia
from Modelo.ModeloFarmacia.Farmacias.forms import FarmaciaForm
from Modelo.ModeloLaboratorio.Laboratorios.models import Laboratorios
from Modelo.ModeloMedicamentos.Medicamentos.models import Medicamento

def registrar_farmacia(request):
    if request.method == 'POST':
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            print(request.POST)
            Farmacia.objects.create(nombre=request.POST['nombre'], direccion=request.POST['direccion'], laboratorios=request.POST['laboratorios'])
            return redirect('home')  # Redirige a una vista de listado
    else:
        form = FarmaciaForm()
    
    return render(request, 'registro_farm.html', {'form': form})

def lista_farm(request):
    farmacias = Farmacia.objects.all() 
    laboratorios=Laboratorios.objects.all()
    medicamentos=Medicamento.objects.all()
    return render(request, 'lista_farm.html', {'farmacias': farmacias, 'medicamentos':medicamentos,'laboratorios':laboratorios})