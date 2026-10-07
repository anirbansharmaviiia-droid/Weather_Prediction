import os

import requests
from django.shortcuts import render
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def home(request):
    weather_data = None
    error = None

    city = request.GET.get("city")

    if city:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "wind_speed": data["wind"]["speed"],
            }

        elif response.status_code == 404:
            error = "City not found. Please enter a valid city name."

        else:
            error = "Unable to get weather data right now."

    return render(
        request,
        "authentication/home.html",
        {
            "weather": weather_data,
            "error": error,
        },
    )