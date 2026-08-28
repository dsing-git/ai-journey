import requests
import json
import time
maximum_retries = 3
delay_between_retries = 2  # seconds

url = "https://api.open-meteo.com/v1/forecast?latitude=28.4595&longitude=77.0266&current_weather=true"
print(f"Fetching weather data from: {url}")

def weather_data(api_response):
    print("Weather data fetched successfully.")
    weather_data = api_response.json()

    current_weather = weather_data.get("current_weather", {})
    print(f"\nCurrent weather data:\n {json.dumps(current_weather, indent=4)}\n")
    temperature = current_weather.get("temperature")
    windspeed = current_weather.get("windspeed")

    print("Current Weather Data:")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {windspeed} km/h")

    with open("current_weather.json", "w") as f:
        json.dump(current_weather, f, indent=4)

    with open("current_weather.txt", "w") as f:
        f.write("--- Gurugram Weather Report ---\n")
        f.write(f"Temperature: {temperature}°C\nWind Speed: {windspeed} km/h")

    print("Data saved to current_weather.json and weather_report.txt")

response = requests.get(url)

if response.status_code == 200:
    weather_data(response)

elif response.status_code == 429:

    while response.status_code == 429 and maximum_retries > 0:
        print(f"Rate limit exceeded. Status code: {response.status_code}. Retrying after {delay_between_retries} seconds...")
        time.sleep(delay_between_retries)
        delay_between_retries *= 2  # Exponential backoff
        response = requests.get(url)
        maximum_retries -= 1
        if response.status_code == 200:
            weather_data(response)
            break
        else:
            print(f"Failed to fetch weather data after retry. Status code: {response.status_code}")

else:
    print(f"Failed to fetch weather data. Status code: {response.status_code}")