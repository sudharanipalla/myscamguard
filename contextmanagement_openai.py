from google import genai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()#load environment variables
API_KEY=os.getenv("YOUR_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

messages = [
    {"role": "system", "content": "You are a career counselor. Give clear, empathetic advice."},
    {"role": "user", "content": "Hi, I'm Nikhil. I enjoy math and programming and I just completed my B.Sc."}
]

response = client.chat.completions.create(
    messages=messages,
    model='gemini-3.6-flash'
)

assistant_reply = response.choices[0].message.content

print("Assistant:", assistant_reply)