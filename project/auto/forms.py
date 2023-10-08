from django import forms

from . import models

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = models.Vehiculo
        fields = ["marca", "modelo", "año"]
        
class BateriaForm(forms.ModelForm):
    class Meta:
        model = models.Bateria
        fields = ["marca", "modelo", "codigo", "valor"]