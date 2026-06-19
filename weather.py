import requests
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter City Name: ")
url = (
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
)

response = requests.get(url)
print(response.json())