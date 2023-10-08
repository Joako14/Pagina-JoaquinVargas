from django.shortcuts import render, redirect

from . import forms, models

def index(request):
    baterias = models.Bateria.objects.all()
    equipos = models.Equipo.objects.all()
    return render(request, "otros/index.html", {"equipos": equipos, "baterias": baterias})

def ingresar_equipo(request):
    if request.method == "POST":
        form = forms.EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("otros:index")
    else:
        form = forms.EquipoForm()
    return render(request, "otros/ingresar_equipo.html", {"form": form})


def ingresar_bateria(request):
    if request.method == "POST":
        form = forms.BateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("otros:index")
    else:
        form = forms.BateriaForm()
    return render(request, "otros/ingresar_bateria.html", {"form": form})