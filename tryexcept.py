import os
import asyncio
from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#load_dotenv()#load environment variables
#API_KEY=os.getenv("YOUR_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",
                           google_api_key="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA",
                           streaming=True)

messages = [
    {"role": "user", "content": "Explain Blackhole in less than 2000 characters"}
]

print("Generating response... \n")

async def stream_response():
    try:
        async for chunk in llm.astream(messages):
           print(chunk.text)
    except Exception as e:
        print("An Error has occured")

asyncio.run(stream_response())

print("Completed Generation of response")

