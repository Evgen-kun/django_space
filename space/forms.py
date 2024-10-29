from django import forms

class UserForm(forms.Form):
    planet_name = forms.CharField(label='Название планеты', max_length=100, required=False)
    satellite_name = forms.CharField(label='Название спутника', max_length=100, required=False)
    research_station_name = forms.CharField(label='Название станции', max_length=100, required=False)

class UserFormCreate(forms.Form):
    planet_name = forms.CharField(label='Название планеты', max_length=100, required=False)
    planet_mass = forms.FloatField(label='Масса планеты', required=False)

    satellite_name = forms.CharField(label='Название спутника', max_length=100, required=False)
    satellite_mass = forms.FloatField(label='Масса спутника', required=False)
    satellite_planet_name = forms.CharField(label='Какой планете принадлежит', max_length=100, required=False)

    research_station_name = forms.CharField(label='Название станции', max_length=100, required=False)
    research_station_planet_name = forms.CharField(label='Какой планете принадлежит', max_length=100, required=False)
    research_station_satellite_name = forms.CharField(label='Какому спутнику принадлежит', max_length=100, required=False)

class UserFormChange(forms.Form):
    planet_id = forms.IntegerField(label='ID', required=False)
    planet_name = forms.CharField(label='Название планеты', max_length=100, required=False)
    planet_mass = forms.FloatField(label='Масса планеты', required=False)

    satellite_id = forms.IntegerField(label='ID', required=False)
    satellite_name = forms.CharField(label='Название спутника', max_length=100, required=False)
    satellite_mass = forms.FloatField(label='Масса спутника', required=False)
    satellite_planet_name = forms.CharField(label='Какой планете принадлежит', max_length=100, required=False)

    research_station_id = forms.IntegerField(label='ID', required=False)
    research_station_name = forms.CharField(label='Название станции', max_length=100, required=False)
    research_station_planet_name = forms.CharField(label='Какой планете принадлежит', max_length=100, required=False)
    research_station_satellite_name = forms.CharField(label='Какому спутнику принадлежит', max_length=100, required=False)