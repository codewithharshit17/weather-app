import requests
import os
from dotenv import load_dotenv

load_dotenv()  

API_KEY = os.getenv("API_KEY")  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition : {description}")
    print(f"Humidity  : {humidity}%")
    print(f"Wind Speed: {wind} m/s")
else:
    print("❌ City not found or API error.")
