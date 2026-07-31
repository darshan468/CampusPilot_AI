from rag.vector_store import load_vector_store


class CampusRetriever:
    """
    CampusPilot AI Retriever

    Responsibilities
    ----------------
    • Load the Chroma vector database
    • Perform semantic search
    • Return the most relevant document chunks
    """

    _retriever = None

    @classmethod
    def get_retriever(cls):
        """
        Load the retriever only once (Singleton).
        """

        if cls._retriever is None:

            vector_store = load_vector_store()

            cls._retriever = vector_store.as_retriever(
                search_type="similarity",
                search_kwargs={
                    "k": 4
                }
            )

        return cls._retriever

    @classmethod
    def retrieve(cls, query: str, k: int = 4):
        """
        Retrieve relevant documents.
        """

        retriever = cls.get_retriever()

        docs = retriever.invoke(query)

        return docs

    @classmethod
    def retrieve_text(cls, query: str, k: int = 4):
        """
        Retrieve relevant documents as plain text.
        """

        docs = cls.retrieve(query, k)

        if not docs:
            return ""

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )