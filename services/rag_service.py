from rag.query import RAGQuery


class RAGService:
    """
    Service layer for CampusPilot RAG.
    """

    def __init__(self):

        self.rag = RAGQuery()

    def search(self, query: str):

        return self.rag.ask(query)