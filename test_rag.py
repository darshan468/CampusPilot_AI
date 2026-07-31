from rag.retriever import CampusRetriever

retriever = CampusRetriever.get_retriever()

while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    docs = retriever.invoke(query)

    print("\nRetrieved Documents:\n")

    for i, doc in enumerate(docs, start=1):

        print("=" * 60)

        print(f"Document {i}")

        print(doc.page_content[:500])