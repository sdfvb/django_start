from django.shortcuts import render
from .models import City
from pip._vendor import requests
from .forms import CityForm


def index(request):
    appid = '5493ef258d707a2785561ade2a80bac3'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)
    contex = {
        'all_info': all_cities,
        'form': form,
    }

    return render(request, 'index.html', contex)
