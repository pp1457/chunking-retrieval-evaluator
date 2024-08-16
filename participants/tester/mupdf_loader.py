import pymupdf4llm
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain.schema.document import Document

def load_document(filename: str) -> list[Document]: 
    md_text = pymupdf4llm.to_markdown(filename)
    print("Converted to Markdown")
    loader = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
        ],
        return_each_line=True
    )
    print("Splitted with Markdown Headers")
    return loader.split_text(md_text)
