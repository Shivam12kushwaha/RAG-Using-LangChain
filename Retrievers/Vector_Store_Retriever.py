from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
# Load API keys from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")



# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),]


# Step 2: Initialize embedding model
# Use HuggingFaceEmbeddings for SemanticChunker (Groq doesn't provide embeddings)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# Step 3: Create Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection")


# Step 4: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)