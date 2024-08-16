from langchain.schema.document import Document

def split_documents(documents: list[Document]) -> list[Document]:
    """By default, mupdf_loader already splits the documents by markdown headers. This function is a pass-through.

    Args:
        documents (list[Document]): List of documents from mupdf_loader

    Returns:
        list[Document]: List of documents
    """
    return documents
