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

def get_current_weather_type():
    if data["cod"] != 200:
        return "unknown"
    main = data["weather"][0]["main"].lower()
    desc = data["weather"][0]["description"].lower()
    if "clear" in main or "ясно" in desc:
        return "sunny"
    elif "cloud" in main or "обла" in desc:
        return "cloudy"
    elif "rain" in main or "дожд" in desc:
        return "rain"
    elif "snow" in main or "снег" in desc:
        return "snow"
    elif "night" in desc or "ночь" in desc:
        return "night"
    elif "day" in desc or "день" in desc:
        return "day"
    else:
        return main
