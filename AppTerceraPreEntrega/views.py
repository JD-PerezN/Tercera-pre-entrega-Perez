from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppTerceraPreEntrega import forms, models

# Create your views here.
def inicio(req):
    return render(req, "AppTerceraPreEntrega/inicio.html")

def videojuegos(req):
    return render(req, "AppTerceraPreEntrega/videojuegos.html")

def series(req):
    return render(req, "AppTerceraPreEntrega/series.html")

def pintura(req):
    return render(req, "AppTerceraPreEntrega/pintura.html")

def musica(req):

    if req.method == "POST":

        musica_form = forms.MusicaForm(req.POST)

        if musica_form.is_valid():
            musica_info = musica_form.cleaned_data
            nueva_musica = models.Musica(
                                        musica=musica_info["musica"],
                                        artista=musica_info["artista"],
                                        genero=musica_info["genero"],
                                        lanzamiento=musica_info["lanzamiento"],
                                        premios=musica_info["premios"])
            nueva_musica.save()
            return redirect("inicio")
    
    else:
        musica_form = forms.MusicaForm()

    return render(req, "AppTerceraPreEntrega/musica.html", {"formulario_musica": musica_form})
