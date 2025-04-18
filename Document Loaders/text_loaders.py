from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq  # Import from Groq instead of OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

import os

load_dotenv()  # Load environment variables from .env file

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing. Please set it in the .env file.")

# Initialize the Groq model (You may need to specify a model name)
model = ChatGroq(model_name="llama3-8b-8192", api_key=groq_api_key)  




prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
