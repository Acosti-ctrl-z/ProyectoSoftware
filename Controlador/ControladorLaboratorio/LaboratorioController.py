from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from Modelo.ModeloLaboratorio.Laboratorios.forms import NuevoLaboratorio
from Modelo.ModeloLaboratorio.Laboratorios.models import Laboratorios

# Create your views here.
def labs(request):
    laboratorio= Laboratorios.objects.all()
    return render(request, 'labs.html', {
        'laboratorio': laboratorio
    })

def crear_labs(request):
    if request.method == 'GET':
        return render(request, 'crear_labs.html', {
                'form': NuevoLaboratorio()
            })
    else:
            Laboratorios.objects.create(nombre=request.POST['nombre'], direccion=request.POST['direccion'])
            return redirect('/labs/')

def modificar_labs(request, id):
    laboratorios = get_object_or_404(Laboratorios, pk=id)
    if request.method == 'POST':
        form = NuevoLaboratorio(request.POST, instance=laboratorios)
        if form.is_valid():
            form.save()
            return redirect('labs')
    else:
        form = NuevoLaboratorio(instance=laboratorios)
    
    return render(request, 'modificar_labs.html', {'form': form, 'lab': laboratorios})