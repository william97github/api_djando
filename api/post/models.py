from django.db import models

# Create your models here.
class Post(models.Model):
    personaje = models.CharField(max_length=50)
    habilidad = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
