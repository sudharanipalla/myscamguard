import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("YOUR_API_KEY")
#API_KEY="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA"

client = genai.Client(api_key=API_KEY)

response=client.models.generate_content(
    model="gemini-3.6-flash",contents="Tell me a story in 100 words.")

print(response.text)
