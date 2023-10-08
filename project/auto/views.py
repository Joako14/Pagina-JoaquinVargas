from django.shortcuts import render, redirect

from . import forms, models

def index(request):
    baterias = models.Bateria.objects.all()
    vehiculos = models.Vehiculo.objects.all()
    return render(request, "auto/index.html", {"vehiculos": vehiculos, "baterias": baterias})

def ingresar_vehiculo(request):
    if request.method == "POST":
        form = forms.VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auto:index")
    else:
        form = forms.VehiculoForm()
    return render(request, "auto/ingresar_vehiculo.html", {"form": form})


def ingresar_bateria(request):
    if request.method == "POST":
        form = forms.BateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auto:index")
    else:
        form = forms.BateriaForm()
    return render(request, "auto/ingresar_bateria.html", {"form": form})
    