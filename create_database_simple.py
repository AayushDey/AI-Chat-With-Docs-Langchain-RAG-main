import os
import shutil
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

CHROMA_PATH = "chroma"
DATA_PATH = "data/books"

def load_markdown_files():
    """Load all markdown files from the DATA_PATH directory."""
    documents = []
    data_dir = Path(DATA_PATH)
    
    for file_path in data_dir.glob("*.md"):
        print(f"Loading {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        doc = Document(
            page_content=content,
            metadata={"source": str(file_path)}
        )
        documents.append(doc)
    
    print(f"Loaded {len(documents)} documents.")
    return documents

def split_text(documents):
    """Split documents into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks

def save_to_chroma(chunks):
    """Save chunks to Chroma database."""
    # Clear existing DB
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
        print(f"Removed existing {CHROMA_PATH} directory.")

    # Save new data with embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    print("Creating Chroma database...")
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def main():
    documents = load_markdown_files()
    chunks = split_text(documents)
    save_to_chroma(chunks)
    print("Database creation complete!")

if __name__ == "__main__":
    main()
