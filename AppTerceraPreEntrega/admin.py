from django.contrib import admin

from AppTerceraPreEntrega import models

# Register your models here.
admin.site.register(models.Videojuegos)
admin.site.register(models.Pintura)
admin.site.register(models.Musica)
admin.site.register(models.Series)