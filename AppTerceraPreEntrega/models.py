from django.db import models

# Create your models here.
class Videojuegos(models.Model):

    videojuego = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    es_digital = models.BooleanField()

class Series(models.Model):

    serie = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    en_emision = models.BooleanField()
    gano_oscar = models.BooleanField()

class Musica(models.Model):

    musica = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    gano_premio = models.BooleanField()

class Pintura(models.Model):

    pintura = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    estilo = models.CharField(max_length=50)
    valor = models.IntegerField()
    en_venta = models.BooleanField()