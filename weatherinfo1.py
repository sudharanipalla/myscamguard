import os
import asyncio
import requests
from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#load_dotenv()#load environment variables
#API_KEY=os.getenv("YOUR_API_KEY")



{

    "name" : "get_weather_info",

    "description": "Fetches the forecast weather for a given city with optional date. Use when user asks about weather, temperature, rain conditions, humidity, whther to take an umbrella or not",

    "parameters": {

        "type": "object",

        "properties": {

            "city": {

                "type": "string",

                "description": "Name of the city for which the weather forecast is required"

            },

            "date": {

                "type": "string",

                "description": "Date for which the weather forecast is required. Format should be YYYY-MM-DD(optional; default: today)"

            }

        },

        "required": ["city"]

    }

}

#ddcf102f017f4436339f1301b5838fab
#https://api.openweathermap.org/data/2.5/weather?q=pune&appid='ddcf102f017f4436339f1301b5838fab'&units=metric


OPENWEATHER_API_KEY="ddcf102f017f4436339f1301b5838fab"




## 3. Function to be called
def get_current_temperature(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data['main']['temp']
    else:
        raise Exception(f"Error fetching weather: {data.get('message', 'Unknown error')}")

get_current_temperature("rome")