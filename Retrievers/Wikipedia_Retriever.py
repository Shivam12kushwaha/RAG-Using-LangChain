from langchain_community.retrievers import WikipediaRetriever
# Initialize the retriever (optional: set language and top_k)
retriever = WikipediaRetriever(top_k_results=2, lang="en")


# Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"
query1 = 'Tell me about love and sufism'

# Get relevant Wikipedia documents
docs = retriever.invoke(query)
docs1 = retriever.invoke(query1)
# Print retrieved content
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") 

for i, doc in enumerate(docs1):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") 