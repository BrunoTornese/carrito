from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField()
    categoria = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.nombre}  {self.precio}'
