from unicodedata import name, numeric
from django import views
from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import *


def index(request):
    form = UserForm(request.POST or None)
    forma = UserFormCreate(request.POST or None)
    formChange = UserFormChange(request.POST or None)
    return render(request, 'index.html', {'form': form, 'forma': forma, 'formChange': formChange})

def all(request):
    planets = Planets.objects.all()
    satellites = Satellites.objects.all()
    research_stations = Research_stations.objects.all()
    return render(request, 'all.html', {'planets': planets, 'satellites': satellites, 'research_stations': research_stations})

def search(request):
    planet = ''
    satellite = ''
    research_station = ''
    
    form= UserForm(request.POST or None)
    if form.is_valid():
        planet_name= form.cleaned_data.get("planet_name")
        satellite_name= form.cleaned_data.get("satellite_name")
        research_station_name= form.cleaned_data.get("research_station_name")

        planet = Planets.objects.filter(name = planet_name)
        if planet:
            planet = planet.get()
        satellite = Satellites.objects.filter(name = satellite_name)
        if satellite:
            satellite = satellite.get()
        research_station = Research_stations.objects.filter(name = research_station_name)
        if research_station:
            research_station = research_station.get()
    
    context= {'title': 'Поиск', 'planet': planet,
              'satellite':satellite, 'research_station':research_station}
    
    return render(request, 'search.html', context)

def create(request):
    planet = satellite = research_station = object

    planet_name = None
    planet_mass = 0

    satellite_name = ''
    satellite_mass = 0
    satellite_planet_name = ''

    research_station_name = ''
    research_station_planet_name = ''
    research_station_satellite_name = ''

    form = UserFormCreate(request.POST or None)
    if form.is_valid():
        planet_name = form.cleaned_data.get("planet_name")
        planet_mass = form.cleaned_data.get("planet_mass")

        satellite_name = form.cleaned_data.get("satellite_name")
        satellite_mass = form.cleaned_data.get("satellite_mass")
        satellite_planet_name = form.cleaned_data.get("satellite_planet_name")

        research_station_name = form.cleaned_data.get("research_station_name")
        research_station_planet_name = form.cleaned_data.get("research_station_planet_name")
        research_station_satellite_name = form.cleaned_data.get("research_station_satellite_name")

        if planet_name and planet_mass:
            planet = Planets(name = planet_name, mass = planet_mass)
            planet.save()
            planet = Planets.objects.filter(name = planet_name).get()

        if satellite_name and satellite_mass and satellite_planet_name:
            satellite = Satellites(name = satellite_name, mass = satellite_mass, planet_name = satellite_planet_name)
            satellite.save()
            satellite = Satellites.objects.filter(name = satellite_name).get()

        if research_station_name and (research_station_planet_name or research_station_satellite_name):
            research_station_planet_name = 'NULL' if len(research_station_planet_name) == 0 else research_station_planet_name
            research_station_satellite_name = 'NULL' if len(research_station_satellite_name) == 0 else research_station_satellite_name
            research_station = Research_stations(name = research_station_name, planet_name = research_station_planet_name, satellite_name = research_station_satellite_name)
            research_station.save()
            research_station = Research_stations.objects.filter(name = research_station_name)

    return render(request, 'search.html', {'title': 'Объекты добавлены', 'planet': planet,
              'satellite':satellite, 'research_station':research_station})

def change(request):
    form = UserFormChange(request.POST or None)
    planet_id = form.cleaned_data.get("planet_id")
    planet = Planets.objects.get(id = planet_id)
    planet.name = form.cleaned_data.get("planet_name")
    planet.mass = form.cleaned_data.get("planet_mass")
    planet.save()
