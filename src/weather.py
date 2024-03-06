import requests


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
