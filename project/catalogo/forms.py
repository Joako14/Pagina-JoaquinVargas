from django import forms
from .models import MarcaCategoria, ModeloCategoria, AñoCategoria

from . import models

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = models.Catalogo
        fields = "__all__"
        
class MarcaCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.MarcaCategoria
        fields = ("marca",)
        
class ModeloCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ModeloCategoria
        fields = ("modelo",)
        
class AñoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.AñoCategoria
        fields = ("año",)
        
class BateriaCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.BateriaCategoria
        fields = "__all__"
        
class ConsultaCatalogoForm(forms.Form):
    marca = forms.ModelChoiceField(queryset=MarcaCategoria.objects.all(), required=False)
    modelo = forms.ModelChoiceField(queryset=ModeloCategoria.objects.all(), required=False)
    año = forms.ModelChoiceField(queryset=AñoCategoria.objects.all(), required=False)
    
        
        
        
