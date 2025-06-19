from django.shortcuts import render
import requests

def home(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'ec75dba00a0f52bbcc75fb62eb29c0f9'
        url = url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get('main'):
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
    return render(request, 'weather/home.html', {'weather': weather_data})
