from django.db import models

class Bateria(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    codigo = models.IntegerField()
    valor = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.codigo} {self.valor}"
    
    
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.año}"