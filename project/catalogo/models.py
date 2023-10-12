from django.db import models
from django.utils import timezone

class MarcaCategoria(models.Model):
    marca = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marca"
        
    def __str__(self) -> str:
        return self.marca
    
class ModeloCategoria(models.Model):
    modelo = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelo"
        
    def __str__(self) -> str:
        return self.modelo
    
class AñoCategoria(models.Model):
    año = models.IntegerField()
    
    class Meta:
        verbose_name = "año"
        verbose_name_plural = "año"
        
    def __str__(self) -> str:
        return f"{self.año}"
    
class BateriaCategoria(models.Model):
    bateria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo_bateria = models.CharField(max_length=100)
    positivo = models.CharField(max_length=100)
    amperaje = models.CharField(max_length=100)
    potencia_arranque = models.CharField(max_length=100)
    tipo_borne = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripcion")
    
    class Meta:
        verbose_name = "bateria"
        verbose_name_plural = "bateria"
        
    def __str__(self) -> str:
        return f"{self.bateria}"
      
    
class Catalogo(models.Model):
    marca = models.ForeignKey(MarcaCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="marca")
    modelo = models.ForeignKey(ModeloCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="modelo")
    año = models.ForeignKey(AñoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="año")
    bateria = models.ForeignKey(BateriaCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="bateria")
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripcion")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualizacion")
    
    class Meta:
        verbose_name = "catalogo"
        verbose_name_plural = "catalogo"
        
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.año} {self.bateria} {self.descripcion}"
    