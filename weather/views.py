from django.shortcuts import render
import requests

def index(request):
    appid = '7fa86abd3da2d37e62f7603cb86cec2a'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid="+appid
    city = 'London'
    return render(request, 'weather/index.html')
