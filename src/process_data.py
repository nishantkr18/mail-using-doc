"""
This module contains the code to:
1. Split the data into chunks (sentences).
2. Create vector embeddings of these sentences.
3. Store them in a vectorstore.
"""
from typing import List
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document

def process_data(docs: List[Document]):
    """
    The function that processes the data.
    """

    # Split into sentences
    source_chunks = []
    splitter = CharacterTextSplitter(
        separator=".", chunk_size=500, chunk_overlap=0)
    for source in docs:
        for chunk in splitter.split_text(source.page_content):
            source_chunks.append(
                Document(page_content=chunk, metadata=source.metadata))

    print('chunks created: ', len(source_chunks))

    # Create vector embeddings and store in vectorstore.
    print('Creating embeddings...')
    embedding = HuggingFaceEmbeddings()

    print('Creating vectorstore...')
    vectorstore = Chroma.from_documents(source_chunks, embedding, persist_directory='./.vectorstore')
    vectorstore.persist()

    return vectorstore
