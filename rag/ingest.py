from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.vector_store import rebuild_vector_store


def ingest_documents():

    print("=" * 60)
    print("CampusPilot AI - RAG Ingestion")
    print("=" * 60)

    print("\nLoading PDF documents...")

    documents = load_documents()

    if not documents:
        print("❌ No PDF documents found.")
        return

    print(f"✅ Loaded {len(documents)} pages")

    print("\nSplitting into chunks...")

    chunks = chunk_documents(documents)

    print(f"✅ Generated {len(chunks)} chunks")

    print("\nCreating Vector Database...")

    rebuild_vector_store(chunks)

    print("\n🎉 RAG Database Created Successfully!")

    print("=" * 60)


if __name__ == "__main__":
    ingest_documents() 