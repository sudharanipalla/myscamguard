from google import genai
from dotenv import load_dotenv
import os

load_dotenv()#load environment variables
API_KEY=os.getenv("YOUR_API_KEY")

client=genai.Client(api_key=API_KEY)
chat=client.chats.create(model="gemini-3.6-flash")

#MESSAGE_1=" I have 2 sons"
MESSAGE_1=input("enter a message:")
response1=chat.send_message(MESSAGE_1)
print(MESSAGE_1)
print(response1.text)

#MESSAGE_2=" How many paws are there in my home"
MESSAGE_2=input("enter a message:")
response2=chat.send_message(MESSAGE_2)
print(MESSAGE_2)
print(response2.text)

print("\nConversational Histoyr")

for message in chat.get_history():

    print(f"{message.role.capitalize()}: {message.parts[0].text}")

    

