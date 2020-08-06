from django.shortcuts import render
from django.views import View

from .models import City
from pip._vendor import requests
from .forms import CityForm


class MainView(View):

    def post(self, request):
        if request.POST.get('mybutton'):
            City.objects.filter(name=request.POST.get('mybutton')).delete()
        else:
            form = CityForm(request.POST)
            if form.is_valid():
                form.save()

        contex = self.api_speaker()
        return render(request, 'index.html', contex)

    def api_speaker(self):
        appid = '5493ef258d707a2785561ade2a80bac3'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid

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
        return  contex

    def get(self, request):
        contex = self.api_speaker()

        return render(request, 'index.html', contex)


