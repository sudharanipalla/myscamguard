import os
import asyncio
import requests
from google.genai import types
from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


weather_function = {
    "name" : "get_current_temperature",
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


    
#API_KEY=os.getenv("YOUR_API_KEY")
OPENWEATHER_API_KEY="ddcf102f017f4436339f1301b5838fab"

client = genai.Client(api_key="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA")
tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

user_prompt = "What is the weather in Mumbai?"

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=user_prompt,
    config=config
)

def get_current_temperature(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data['main']['temp']
    else:
        raise Exception(f"Error fetching weather: {data.get('message', 'Unknown error')}")
    
    
first_part = response.candidates[0].content.parts[0]

if first_part.function_call.name == "get_current_temperature":

    temperature = get_current_temperature(first_part.function_call.args.get("city"))
    print(temperature)