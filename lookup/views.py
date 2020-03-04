from django.shortcuts import render

# Create your views here.


def home(request):
    import json
    import requests

    if request.method == "POST":
        location = request.POST['location']
        api_req = requests.get("http://api.waqi.info/feed/"+location+"/?token=56b182a94aa9eb6fae0ebbc1fa0c2f47111bbf34")
        try:
            api = api_req.json()
        except Exception as e:
            api = "Error...."
        if api['data']['aqi'] <= 50:
            AQI_Quality = "Good"
            category_color = "good"
        elif api['data']['aqi'] <= 100:
            AQI_Quality = "Moderate"
            category_color = "moderate"
        elif api['data']['aqi'] <= 150:
            AQI_Quality = "Unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api['data']['aqi'] <= 200:
            AQI_Quality = "Unhealthy"
            category_color = "unhealthy"
        elif api['data']['aqi'] <= 300:
            AQI_Quality = "Very unhealthy"
            category_color = "very_unhealthy"
        else:
            AQI_Quality = "Hazardous"
            category_color = "hazardous"
        return render(request, 'home.html', {'api': api, 'AQI_Quality': AQI_Quality, 'category_color': category_color})
    else:
        api_req = requests.get("http://api.waqi.info/feed/cambodia/?token=56b182a94aa9eb6fae0ebbc1fa0c2f47111bbf34")
        try:
            api = api_req.json()
        except Exception as e:
            api = "Error...."

        if api['data']['aqi'] <= 50:
            AQI_Quality = "Good"
            category_color = "good"
        elif api['data']['aqi'] <= 100:
            AQI_Quality = "Moderate"
            category_color = "moderate"
        elif api['data']['aqi'] <= 150:
            AQI_Quality = "Unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api['data']['aqi'] <= 200:
            AQI_Quality = "Unhealthy"
            category_color = "unhealthy"
        elif api['data']['aqi'] <= 300:
            AQI_Quality = "Very unhealthy"
            category_color = "very_unhealthy"
        else:
            AQI_Quality = "Hazardous"
            category_color = "hazardous"
        return render(request, 'home.html', {'api':api, 'AQI_Quality':AQI_Quality, 'category_color':category_color})


def about(request):
    return render(request, 'about.html', {})
