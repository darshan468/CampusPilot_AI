class RAGTool:
    """
    ==========================================================
    CampusPilot AI - RAG Tool
    ==========================================================

    Responsibilities
    ----------------
    • Search the knowledge base
    • Return relevant information
    • Update workflow state
    """

    def __init__(self, rag_service):

        self.rag_service = rag_service

    def search(self, query: str):

        try:

            return self.rag_service.search(query)

        except Exception as e:

            return (
                "❌ Failed to search the knowledge base.\n\n"
                f"{str(e)}"
            )

    def process(self, state):

        try:

            query = state.get("query", "").strip()

            if not query:

                state["error"] = "Query cannot be empty."

                return state

            answer = self.search(query)

            state["rag_response"] = answer

            state.setdefault("responses", []).append(answer)

            state.setdefault("agent_results", {})["rag"] = answer

            return state

        except Exception as e:

            state["error"] = (
                f"RAG Tool Error:\n\n{str(e)}"
            )

            return state