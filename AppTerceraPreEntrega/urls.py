from django.urls import path

from AppTerceraPreEntrega import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("videojuegos/", views.videojuegos, name="videojuegos"),
    path("musica/", views.musica, name="musica"),
    path("pintura/", views.pintura, name="pintura"),
    path("series/", views.series, name="series"),
    path("busqueda-premios/", views.busqueda_premios, name="busqueda-premios"),
    path("buscar-premios/", views.buscar_premios, name="buscar-premios"),
    path("busqueda-coleccion/", views.busqueda_coleccion, name="busqueda-coleccion"),
    path("buscar-coleccion/", views.buscar_coleccion, name="buscar-coleccion"),
    path("busqueda-valor/", views.busqueda_valor, name="busqueda-valor"),
    path("buscar-valor/", views.buscar_valor, name="buscar-valor")
]