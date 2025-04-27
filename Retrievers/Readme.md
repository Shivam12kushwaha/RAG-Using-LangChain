# Retrievers in LangChain
## What are Retrievers?
#### A Retriever is a component in LangChain that fetches relevant document from a data source in respeonse to a user's query.
#### There are multiple types of Retrievers.
#### All Retrievers in LangChain are Runnables.
## Types of Retrievers
### (1) Wikipedia Retriever:
#### A Wikipedia Retriever is a retriever that queries the wikipedia API to fetch relevant content for a given query.
### (2) Vector Store Retriever:
#### A Vector Store  retriever in LangChain is the most common type of retriever that lets you search and fetch documnets from a vector store based on semantic similarity usung vector embeddings.
### (3) Maximum Marginal Relevance(MMR):
#### MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaning high relevance of the query.
### (4) Multi-Query Retriever:
#### Sometimes a single query might not capture all the ways information is phrased in your documents.
### (5) Contextual Compression Retriever:
#### The Contextual Compression Retriever in LangChain is an advanced retriever that improves retrieval quality by compressing documents after retrieval-keeping only the relevant content based on the user's query.
### More Retrievers:
#### BM25Retriever, ParentDocumentRetriever, SelfQueryRetriever, TimeWeightedRetriever, EnsembleRetriever, ArxivRetriever, MultiVectorRetriver
