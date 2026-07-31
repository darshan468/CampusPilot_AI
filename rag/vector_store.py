from pathlib import Path

from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


# Directory to store Chroma database
CHROMA_DB = Path("rag/chroma_db")


def create_vector_store(chunks):
    """
    Create a new Chroma vector database from document chunks.
    """

    # Create directory if it doesn't exist
    CHROMA_DB.mkdir(parents=True, exist_ok=True)

    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DB)
    )

    print(f"✅ Vector database created successfully!")
    print(f"📁 Saved at: {CHROMA_DB}")

    return vector_store


def load_vector_store():
    """
    Load an existing Chroma vector database.
    """

    if not CHROMA_DB.exists():
        raise FileNotFoundError(
            "❌ Chroma database not found.\n"
            "Run 'python rag/ingest.py' first."
        )

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=str(CHROMA_DB),
        embedding_function=embeddings
    )

    return vector_store


def delete_vector_store():
    """
    Delete the existing Chroma database.
    Useful when rebuilding after adding new PDFs.
    """

    import shutil

    if CHROMA_DB.exists():
        shutil.rmtree(CHROMA_DB)
        print("🗑 Existing Chroma database deleted.")
    else:
        print("No Chroma database found.")


def rebuild_vector_store(chunks):
    """
    Delete the old database and create a fresh one.
    """

    delete_vector_store()
    return create_vector_store(chunks)