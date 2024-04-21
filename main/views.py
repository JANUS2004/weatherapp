from django.shortcuts import render
import urllib.request
import json
from .models import Weather

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' 
            + city + '&appid=bd9813a0c82f1bc9a2f3b8a0ed96a744').read()
        
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }

        temperature = float(data['temp'])  # Convert temperature to float
        # Saving weather data to the database
        Wdata = Weather.objects.create(
            city=city,
            country_code=str(list_of_data['sys']['country']),
            temperature=str(list_of_data['main']['temp']) + 'k',
            humidity=str(list_of_data['main']['humidity'])
        )

        # Retrieving all weather data from the database and ordering by temperature
        bdata = Weather.objects.all().order_by('timestamp')

        # Pass both data and bdata to the template
        return render(request, "index.html", {"data": data, "bdata": bdata})
    else:
        return render(request, "index.html", {})
