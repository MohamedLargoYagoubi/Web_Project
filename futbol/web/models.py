from django.db import models

# Create your models here.
class Liga(models.Model):
    name = models.CharField(max_length=256)
    
class Equipo(models.Model):
    name = models.CharField(max_length=256)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

class Tabla(models.Model):
    name = models.CharField(max_length=256)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

class Jugador(models.Model):
    name = models.CharField(max_length=256)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
