from django.db import models

# Create your models here.
class Videojuegos(models.Model):

    videojuego = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    coleccion = models.IntegerField()

class Series(models.Model):

    serie = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    plataforma = models.CharField(max_length=50)

class Musica(models.Model):

    musica = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    premios = models.IntegerField(default=0)

class Pintura(models.Model):

    pintura = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    estilo = models.CharField(max_length=50)
    valor = models.IntegerField()