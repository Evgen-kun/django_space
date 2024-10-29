from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models import *


class SpaceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    list_display_links = ['timestamp', 'updated']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']
    list_editable = ['title']

    class Meta:
        model = Space

class PlanetsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mass']
    list_display_links = ['mass']
    list_filter = ['id', 'name']
    search_fields = ['name']
    list_editable = ['name']

    class Meta:
        model = Planets

class SatellitesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mass', 'planet_name']
    list_display_links = ['mass', 'planet_name']
    list_filter = ['id', 'name', 'planet_name']
    search_fields = ['name']
    list_editable = ['name']

    class Meta:
        model = Satellites

class Research_stationsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'planet_name', 'satellite_name']
    list_display_links = ['planet_name', 'satellite_name']
    list_filter = ['id', 'name', 'planet_name', 'satellite_name']
    search_fields = ['name']
    list_editable = ['name']

    class Meta:
        model = Research_stations

admin.site.register(Space, SpaceModelAdmin)
admin.site.register(Planets, PlanetsModelAdmin)
admin.site.register(Satellites, SatellitesModelAdmin)
admin.site.register(Research_stations, Research_stationsModelAdmin)