from langchain_experimental.text_splitter import SemanticChunker
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function

def split_documents(documents: list[Document]):
    text_splitter = SemanticChunker(
        get_embedding_function(), breakpoint_threshold_type="percentile")
    return text_splitter.split_documents(documents)

