from django.db import models

# Create your models here.

# Se crea los modelos de la DB

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre