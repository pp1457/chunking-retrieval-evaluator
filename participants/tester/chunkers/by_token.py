from langchain_text_splitters import TokenTextSplitter
from langchain.schema.document import Document

def split_documents(documents: list[Document]) -> list[Document]:
    text_splitter = TokenTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
    )
    return text_splitter.split_documents(documents)
