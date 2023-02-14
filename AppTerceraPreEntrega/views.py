from django.shortcuts import render

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
    return render(req, "AppTerceraPreEntrega/musica.html")
