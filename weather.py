import requests
import os
from dotenv import load_dotenv
from pprint import pprint

#load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter City Name: ")
url = (
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
)

response = requests.get(url)
data=response.json()
pprint(data)

if response.status_code == 200:
    temperature = data["main"]["temp"]

    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]

    weather = data["weather"][0]["description"]

    wind_speed = data["wind"]["speed"]

    print("\n" + "=" * 35)

    print("Weather Report")

    print("=" * 35)

    print(f"City: {city}")

    print(f"Temperature: {temperature}°C")

    print(f"Feels Like: {feels_like}°C")

    print(f"Humidity: {humidity}%")

    print(f"Condition: {weather}")

    print(f"Wind Speed: {wind_speed} m/s")

    print("=" * 35)
else:
    print("City not found")