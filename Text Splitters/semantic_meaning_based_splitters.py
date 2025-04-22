from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Use HuggingFaceEmbeddings for SemanticChunker (Groq doesn't provide embeddings)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Semantic chunker using local embeddings
text_splitter = SemanticChunker(
    embedding_model,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

# Sample text
sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

# Split text semantically
docs = text_splitter.create_documents([sample])

# Print chunk info
print(f"Number of chunks: {len(docs)}")
for i, doc in enumerate(docs):
    print(f"\n--- Chunk {i+1} ---\n{doc.page_content}\n")


