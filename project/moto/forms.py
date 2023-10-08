from django import forms

from . import models

class MotocicletaForm(forms.ModelForm):
    class Meta:
        model = models.Motocicleta
        fields = ["marca", "modelo", "año"]
        
class BateriaForm(forms.ModelForm):
    class Meta:
        model = models.Bateria
        fields = ["marca", "modelo", "codigo", "valor"]