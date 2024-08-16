from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain_chroma import Chroma
from mupdf_loader import load_document
from chunkers.semantic import split_documents
from dotenv import load_dotenv
from os import environ

load_dotenv()

CHROMA_PATH = "chroma"

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, 
        embedding_function=get_embedding_function()
    )
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    chunks_with_ids = calculate_chunk_ids(chunks)

    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            print(f"\nChunk {chunk.metadata["id"]}: ")
            print(chunk.page_content)
            new_chunks.append(chunk)
    
    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunks_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunks_ids)
    else:
        print("✅ No new documents to add")


def calculate_chunk_ids(chunks):
    current_chunk_index = 0

    for chunk in chunks:
        source = environ.get('SOURCE', 'unk')
        current_chunk_index += 1

#    if (current_page_id == last_page_id):
#    else:
#       current_chunk_index = 0

        chunk_id = f"{source}:{current_chunk_index}"
        chunk.metadata["id"] = chunk_id 
  
    return chunks

if __name__ == "__main__":
    documents = load_document(environ.get("SOURCE", "unk"))

    chunks = split_documents(documents)

    print("Documents Splitted")

    add_to_chroma(chunks)


