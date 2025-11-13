
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    clima = data["current_weather"]
    print("Temperatura actual:", clima["temperature"], "°C")
    print("Velocidad del viento:", clima["windspeed"], "km/h")
else:
    print("Error al obtener los datos. Código:", response.status_code)
