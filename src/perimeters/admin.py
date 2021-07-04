from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Perimeter


class PerimeterAdmin(LeafletGeoAdmin):
    search_fields = ('name', 'insee')


admin.site.register(Perimeter, PerimeterAdmin)
