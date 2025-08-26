import requests
import load_config

API_KEY = load_config.Load_API()

CITY = load_config.load_sity()

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(url)
data = response.json()

def weather_temp_desc():
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        out = {"temp": str(temp), "desc": str(desc)}
        return out
    else:
        print("Город не найден")
