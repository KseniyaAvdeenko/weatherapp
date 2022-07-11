from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '7fa86abd3da2d37e62f7603cb86cec2a'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid
    
    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name, 
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'wind': res['wind']['speed'],
            "pressure": res["main"]['pressure'],
            'humidity': res['main']['humidity']
        }

        all_cities.append(city_info)

    if (request.method=="post"):
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    context = {
        'all_info': all_cities, 'form':form
    }
    
    return render(request, 'weather/index.html', context)
