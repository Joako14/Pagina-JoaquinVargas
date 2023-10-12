from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

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