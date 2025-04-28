# RAG:
#### RAG is a technique that combines information retrieval with the language generation , where a model retrieves relevant documents from a knowledge base and then uses tehm as context to generate accurate and grounded response.
## Benefits of using RAG:
#### 1. Use of up-to-date information.
#### 2. Better Privacy
#### 3. No limit of document size.
## Components of RAG:
#### (1) Document Loaders   (2) Text Spiltters (3) Vector Databases (4) Retrievers
### Most commonly used document loaders are:
#### (1) Text Loader (2) PyPDF Loader (3) WebBase Loader (4) CSV Loader
### ** RAG is way to make a language model like ChatGPT smarter by giving it extra information at the time you ask your question.
## Understanding RAG:
#### Rag can be divided into 4 steps-
#### (a) Indexing (b) Retrieval (c) Augmentation (d) Generation
## (a) Indexing:
#### Indexing is the process of preparing your knowledge base so that it can be efficiently searched at query time. This step consists of 4 sub-steps-
#### Document Ingestion, Text Chunking, Embedding Generation, Storage in vector Store.
## (b) Retrieval:
#### It is the real time process of finding the most relevant pieces of information from a pre-built index based on the user's question.
## (c) Augmentation:
#### Augmentation refers to the step where the retrieved documents(chunks of relevant context) are combined with user's query to form a new enriched prompt for the LLM.
## (d) Generation:
#### Generation is the final step where a LLM uses the user's query and the retrieved and augmented context to generate response.
