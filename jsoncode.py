from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

format_instructions = parser.get_format_instructions()

resume_text = "My name is Prachi, I am 20 years old and my email is prachi@gmail.com"

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash",
                             google_api_key="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA")

response = llm.invoke(f"""
Extract the information in a strict JSON format
Text: {resume_text}
JSON:
""")

parser.parse(response.text)
print(response.text)