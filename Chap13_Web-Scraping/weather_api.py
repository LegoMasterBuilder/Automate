import requests
import json
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_current_weather():
    city_name = 'San Francisco'
    state_code = 'CA'
    country_code = 'US'

    response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={os.getenv("api_key")}')
    print(response.text)

    response_data = json.loads(response.text)
    print(response.data)

    lat = json.loads(response.text[0]['lat'])
    lon = json.loads(response.text[0]['lon'])
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
    response_data = json.loads(response.text)
    print(response_data)

    kelvin = response_data['main']['temp']
    print(kelvin)

    # Convert Kelvin to Celsius
    print(round(kelvin - 273.15, 1))

    # Convert Kelvin to Fahrenheit
    print(round(kelvin * (9 / 5) - 459.67, 1))
    

def main():
    configure()
    get_current_weather()

main()