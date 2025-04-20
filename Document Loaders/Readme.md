# (1) Text Loaders:
#### Text Loader is a simple and commonly used document loader in LangChain that reads plain text(.txt) files and converts them into LangChain Document objects.
## Use Case:
#### Ideal for loading chat logs, scrapted text, transcripts, code snippets or any plain text data into a LangChain Pipeline.
## Limitations:
#### Works only with .txt files

# (2) PyPDF Loaders:
#### PyPDF Loader is a document loader in LangChain used to load content from PDF files and convert each page into a document object.
## Limitations:
#### It uses the PyPDF library under the hood - not great with scanned PDFs or complex layouts. 

# (3) Web Base Loader:
#### Web Base Loader is a document loader in LangChain used to load and extract from webpages(URLs). It uses BeautifulSoup under the hood to parse HTML and extract visible text.
## When To Use?
#### For blogs, newws articles or public websites where the content is primarily text based stattic.
## Limitations:
#### (a) Does not handle JAva Script-heavy pages well(use Selenium Loader for that)
#### (b) Loads only static content(what is in the HTML, not what loads after the page renders.

# (4) CSV Loader:
#### CSV Loader is a document loader used to load csv files into LangChain Document Objects-one per row by default.
