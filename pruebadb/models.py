from django.db import models

# Create your models here.

class Bloque(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

