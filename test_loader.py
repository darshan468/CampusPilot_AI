from rag.loader import load_documents

docs = load_documents()

print(len(docs))

print(docs[0].page_content[:500])