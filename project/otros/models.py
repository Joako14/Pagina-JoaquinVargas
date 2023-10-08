from django.db import models

class Bateria(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    codigo = models.IntegerField()
    valor = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.codigo} {self.valor}"
    
    
class Equipo(models.Model):
    equipo = models.CharField(max_length=100)
    tipo_de_bateria = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.equipo} {self.tipo_de_bateria}"