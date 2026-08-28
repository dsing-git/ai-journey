import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=28.4595&longitude=77.0266&current_weather=true"
print(f"Fetching weather data from: {url}")

response = requests.get(url)

if response.status_code == 200:
    print("\nWeather data fetched successfully.")
    weather_data = response.json()
    #print(f"Weather data: {json.dumps(weather_data, indent=4)}\n")

    current_weather = weather_data.get("current_weather", {})
    print (f"\nCurrent weather data:\n {json.dumps(current_weather, indent=4)}\n")
    temperature = current_weather.get("temperature")
    windspeed = current_weather.get("windspeed")

    print("Current Weather Data:")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {windspeed} km/h")

else:
    print(f"Failed to fetch weather data. Status code: {response.status_code}")