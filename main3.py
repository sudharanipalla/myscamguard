import os
import asyncio
from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()#load environment variables
API_KEY=os.getenv("YOUR_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",google_api_key="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA")
response=llm.invoke("what is the capital of France")
print(response.content)

