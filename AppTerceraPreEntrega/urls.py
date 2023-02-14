from django.urls import path

from AppTerceraPreEntrega import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("videojuegos/", views.videojuegos, name="videojuegos"),
    path("musica/", views.musica, name="musica"),
    path("pintura/", views.pintura, name="pintura"),
    path("series/", views.series, name="series")
]