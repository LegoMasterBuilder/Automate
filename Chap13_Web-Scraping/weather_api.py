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

    response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={os.getenv('api_key')}')
    print(response.text)

    response_data = json.loads(response.text)
    print(response.data)

def main():
    configure()
    get_current_weather()

main()