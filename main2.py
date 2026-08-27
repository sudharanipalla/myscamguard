import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("YOUR_API_KEY")

client = genai.Client(api_key=API_KEY)

response=client.models.generate_content(
    model="gemini-3.6-flash",contents="Explain Blackhole in less than 2000 characters")

print("Generating response... \n")

async def stream_response():
    try:
        async for chunk in response:
           print(chunk.text)
        #print(response.text)
    except Exception as e:
            print("An Error has occured")
#await stream_response()

print("Completed Generation of response")
