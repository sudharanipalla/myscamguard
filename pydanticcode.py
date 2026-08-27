from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(description="The age of the person")
    email: str = Field(description="The email of the person")

parser = PydanticOutputParser(pydantic_object=Person)

resume_text = "My name is Prachi, I am 20 years old and my email is prachi@gmail.com"

format_instructions = parser.get_format_instructions()

prompt = """
Extract the information in a strict JSON format
Text: {resume}
JSON:
{format_instructions}
"""

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash",
                             google_api_key="")

response = llm.invoke(prompt.format(resume=resume_text, format_instructions=format_instructions))

parser.parse(response.text)
print(response.text)
