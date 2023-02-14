from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppTerceraPreEntrega import forms, models

# Create your views here.
def inicio(req):
    return render(req, "AppTerceraPreEntrega/inicio.html")

def videojuegos(req):

    if req.method == "POST":

        videojuegos_form = forms.VideojuegosForm(req.POST)

        if videojuegos_form.is_valid():
            videojuegos_info = videojuegos_form.cleaned_data
            nuevo_videojuego = models.Videojuegos(
                                        videojuego=videojuegos_info["videojuego"],
                                        consola=videojuegos_info["consola"],
                                        genero=videojuegos_info["genero"],
                                        coleccion=videojuegos_info["coleccion"])
            nuevo_videojuego.save()
            return redirect("inicio")
    
    else:
        videojuegos_form = forms.VideojuegosForm()

    return render(req, "AppTerceraPreEntrega/videojuegos.html", {"formulario_videojuegos": videojuegos_form})

def series(req):

    if req.method == "POST":

        series_form = forms.SeriesForm(req.POST)

        if series_form.is_valid():
            series_info = series_form.cleaned_data
            nueva_series = models.Series(
                                        serie=series_info["serie"],
                                        lanzamiento=series_info["lanzamiento"],
                                        plataforma=series_info["plataforma"])
            nueva_series.save()
            return redirect("inicio")
    
    else:
        series_form = forms.SeriesForm()

    return render(req, "AppTerceraPreEntrega/series.html", {"formulario_series": series_form})


def pintura(req):

    if req.method == "POST":

        pintura_form = forms.PinturaForm(req.POST)

        if pintura_form.is_valid():
            pintura_info = pintura_form.cleaned_data
            nueva_pintura = models.Pintura(
                                        pintura=pintura_info["pintura"],
                                        autor=pintura_info["autor"],
                                        estilo=pintura_info["estilo"],
                                        valor=pintura_info["valor"])
            nueva_pintura.save()
            return redirect("inicio")
    
    else:
        pintura_form = forms.PinturaForm()

    return render(req, "AppTerceraPreEntrega/pintura.html", {"formulario_pintura": pintura_form})

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

def busqueda_premios(req):
    return render(req, "AppTerceraPreEntrega/busqueda-premios.html")

def buscar(req):
    if req.GET["premios"]:
        premios = req.GET["premios"]
        musica = models.Musica.objects.filter(premios__icontains=premios)

        return render(req, 'AppTerceraPreEntrega/result-busqueda-premios.html', {"musica": musica, "premios": premios})
    
    else:
        respuesta = "No se encuentra"

    return HttpResponse(respuesta)
