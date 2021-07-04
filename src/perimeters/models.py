from django.contrib.gis.db import models


class Perimeter(models.Model):
    name = models.CharField("Nom", max_length=128)
    insee = models.CharField("code INSEE", max_length=16)
    wikipedia = models.CharField("wikipedia", max_length=255)
    poly = models.MultiPolygonField()

    def __str__(self):
        return self.name
