from django.db import models

# Create your models here.
class Liga(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Equipo(models.Model):
    name = models.CharField(max_length=256)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tabla(models.Model):
    name = models.CharField(max_length=256)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name

class Jugador(models.Model):
    name = models.CharField(max_length=256)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name
