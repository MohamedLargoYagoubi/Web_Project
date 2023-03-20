from django.db import models

# Create your models here.
class Jugador(models.Model):
    name = models.CharField(max_length=256)

class Equipo(models.Model):
    name = models.CharField(max_length=256)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)

class Tabla(models.Model):
    name = models.CharField(max_length=256)
    equips = models.ForeignKey(Equipo, on_delete=models.CASCADE)


class Liga(models.Model):
    name = models.CharField(max_length=256)
    tabla = models.ForeignKey(Tabla, on_delete=models.CASCADE)
