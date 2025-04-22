### Text Splitting is a process of breaking large chunks of text like articles,PDFs,HTML pages or books into smaller, managable pieces(chunks) that an LLM can handle effectively.

## Overcoming model limitations:
#### Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.

## Downstream Tasks:
#### Text Splitting improves nearly every LLM powered task.

## (1) Length Based Splitting:
#### In langChain, Lenght Based Splitting is handled by the CharacterTextSplitter class or its variants where you can define how long each chunk of text should be. This is especially useful when working with large documents that need to be processed by language models with taken or character limits. 
## (2) Text-Structured Based Splitting:
#### Structured Splitting uses the document inherent layout like headings, lists or markdown structure to break it into meaningful chunks rather than just by length or tokens.
## (3) Document Structured Based Splitting:
#### Instead of splitting text blindly by length, document-structured splitting leverages format-specific such as Sections, Metadata, Pages, Paragraph, Visual Layouts(PDFs or HTML), Codes(Python, Markdown, JAVA....)
## (4) Semantic Meaning Based Text Splitters:
#### In Semantic Meaning Based Text Splitting, chunks are not cut by length, headers or pages they are decided by meaningful contexts like sentences, paragraphs and natural structure. These splitters use natural language cues to split text while trying to preserve contextual integrity. They don't just split after n characters, they aim to split where it makes sense lingustically.
