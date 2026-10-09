import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return "Sorry, city not found."

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return (
            f"The weather in {city} is "
            f"{description} with temperature {temperature} degree Celsius."
        )

    except Exception as e:
        return "Unable to fetch weather information."