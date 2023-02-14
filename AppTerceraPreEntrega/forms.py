from django import forms

class VideojuegosForm(forms.Form):

    videojuego = forms.CharField()
    consola = forms.CharField()
    genero = forms.CharField()
    coleccion = forms.IntegerField()

class SeriesForm(forms.Form):

    serie = forms.CharField()
    lanzamiento = forms.DateField()
    plataforma = forms.CharField()

class MusicaForm(forms.Form):

    musica = forms.CharField()
    artista = forms.CharField()
    genero = forms.CharField()
    lanzamiento = forms.DateField()
    premios = forms.IntegerField()

class PinturaForm(forms.Form):

    pintura = forms.CharField()
    autor = forms.CharField()
    estilo = forms.CharField()
    valor = forms.IntegerField()