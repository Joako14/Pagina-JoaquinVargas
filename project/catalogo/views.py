from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ConsultaCatalogoForm
from .models import BateriaCategoria, Catalogo

from . import models, forms

class CatalogoList(ListView):
    model = models.Catalogo
    
class CatalogoDetail(DetailView):
    model = models.Catalogo
    
class CatalogoCreate(CreateView):
    model = models.Catalogo
    form_class = forms.CatalogoForm
    success_url = reverse_lazy("catalogo:catalogo_list")
    
class MarcaCategoriaCreate(CreateView):
    model = models.MarcaCategoria
    form_class = forms.MarcaCategoriaForm
    success_url = reverse_lazy("catalogo:index")
       
class ModeloCategoriaCreate(CreateView):
    model = models.ModeloCategoria
    form_class = forms.ModeloCategoriaForm
    success_url = reverse_lazy("catalogo:index")

class AñoCategoriaCreate(CreateView):
    model = models.AñoCategoria
    form_class = forms.AñoCategoriaForm
    success_url = reverse_lazy("catalogo:index")
    
class BateriaCategoriaCreate(CreateView):
    model = models.BateriaCategoria
    form_class = forms.BateriaCategoriaForm
    success_url = reverse_lazy("catalogo:index")
    
class CatalogoUpdate(UpdateView):
    model = models.Catalogo
    form_class = forms.CatalogoForm
    success_url = reverse_lazy("catalogo:catalogo_list")
    
class CatalogoDelete(DeleteView):
    model = models.Catalogo
    success_url = reverse_lazy("catalogo:catalogo_list")
    
def consulta_catalogo(request):
    resultados = None
    detalles_bateria = []
    form = ConsultaCatalogoForm()
    
    if request.method == 'POST':
        form = ConsultaCatalogoForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data.get('marca')
            modelo = form.cleaned_data.get('modelo')
            año = form.cleaned_data.get('año')
            
            # Realiza la consulta en función de los valores seleccionados
            resultados = Catalogo.objects.filter(marca=marca, modelo=modelo, año=año)
            detalles_bateria = [item.bateria for item in resultados]

    return render(request, 'catalogo/consulta_catalogo.html', {'form': form, 'resultados': resultados, 'detalles_bateria': detalles_bateria})




