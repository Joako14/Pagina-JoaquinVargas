from django import forms

from . import models

class EquipoForm(forms.ModelForm):
    class Meta:
        model = models.Equipo
        fields = ["equipo", "tipo_de_bateria"]
        
class BateriaForm(forms.ModelForm):
    class Meta:
        model = models.Bateria
        fields = ["marca", "modelo", "codigo", "valor"]