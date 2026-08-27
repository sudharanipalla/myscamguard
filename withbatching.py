import os
import asyncio
from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#load_dotenv()#load environment variables
#API_KEY=os.getenv("YOUR_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",
                           google_api_key="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA"
                           )
prompts = [
    "Summarize the history of the internet in 3 lines.",
    "Explain what blockchain is for a beginner.",
    "What are the main components of a neural network?",
    "Give three use-cases of artificial intelligence in education.",
    "Describe the importance of data privacy in healthcare systems."
]

responses = llm.batch(prompts)

for i, response in enumerate(responses):
    print(f"\n Prompt {i+1}: {prompts[i]}")
    print(f"\n Response: {response.text}")
    print("\n ----------- \n")