from django.shortcuts import render, redirect

from . import forms, models

def index(request):
    baterias = models.Bateria.objects.all()
    motocicletas = models.Motocicleta.objects.all()
    return render(request, "moto/index.html", {"motocicletas": motocicletas, "baterias": baterias})

def ingresar_motocicleta(request):
    if request.method == "POST":
        form = forms.MotocicletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("moto:index")
    else:
        form = forms.MotocicletaForm()
    return render(request, "moto/ingresar_motocicleta.html", {"form": form})


def ingresar_bateria(request):
    if request.method == "POST":
        form = forms.BateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("moto:index")
    else:
        form = forms.BateriaForm()
    return render(request, "moto/ingresar_bateria.html", {"form": form})