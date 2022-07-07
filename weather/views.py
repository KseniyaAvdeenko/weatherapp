from django.shortcuts import render
import requests

def index(request):
    appid = '7fa86abd3da2d37e62f7603cb86cec2a'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid
    city = 'Tokyo'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city, 
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'wind': res['wind']['speed'],
        "pressure": res["main"]['pressure'],
        'humidity': res['main']['humidity']
    }
    context = {
        'info': city_info
    }
    return render(request, 'weather/index.html', context)
