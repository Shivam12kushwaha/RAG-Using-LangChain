### A Vector Store is a system designed to store and retrieve data represented as numerical vectors.
## Key Features:
### (1) Storage:
#### Ensures that vectors and their associated metadata are retained, whether in-memory for quick lookups or on-disk for durability and large scale use.
### (2) Similarity Search:
#### Helps retrieve the vectors most similar to a query vector.
### (3) Indexing:
#### Provide a data structure or method that enables fast similarity searches on high-dimensional vector(eg., approximate nearest neighbour lookups)
### (4) CRUD Operations:
#### Manage the lifecycle of data adding new vectors, reading them updating existing entries, removing outdated vectors.
### Use Cases:
#### Semantic Search, RAG, Recommender System, Image or Multimedia Search.
# Vector Stores in LangChain:
## Suppoerted Stored:
#### LangChain integrates with the multiple vector stores FAISS, Pinecone, Chroma, Qdrant, Weaviate ect., giving you flexibility in scale, features and deployment.
## Common Interface:
#### A uniform Vector Store API lets you swap out one backend(eg,. FAISS) for another(eg,. Pinecone) with minimal code changes.
## Meta Data Handling:
#### Most Vector stores in LangChain allow you to attach metadata(eg,. Timestamp, Authors) to each document, enabling filtering based retrieval.
# Chroma Vector Store:
### Chroma is a lightweight, open source vector data base that especially friendly for local developement and small to medium-scale prediction needs.
