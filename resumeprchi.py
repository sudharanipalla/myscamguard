from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

parser=JsonOutputParser()
format_instructions=parser.get_format_instructions()

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",google_api_key="AQ.Ab8RN6L1V3l5Ki6f8xy3SsF3si2IXt0mZBJHu6pnA5kn4hLIMA")
resume_text=