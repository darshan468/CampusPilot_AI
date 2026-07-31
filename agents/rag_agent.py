from core.llm import llm
from rag.retriever import CampusRetriever


class RAGAgent:
    """
    CampusPilot AI - RAG Agent
    """

    def __init__(self, rag_tool=None):
        self.rag_tool = rag_tool

    def process(self, query: str) -> str:
        """
        Answer a user query using the uploaded college documents.
        """

        try:

            retriever = CampusRetriever.get_retriever()

            docs = retriever.invoke(query)

            if not docs:

                return (
                    "❌ I couldn't find any relevant information "
                    "in the uploaded college documents."
                )

            # Build context
            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            # Collect sources
            sources = []

            for doc in docs:

                source = doc.metadata.get(
                    "source",
                    "Unknown Document"
                )

                source = source.split("\\")[-1]

                if source not in sources:
                    sources.append(source)

            prompt = f"""
You are CampusPilot AI.

Answer ONLY using the provided context.

Context:

{context}

Question:

{query}

Answer:
"""

            answer = llm.generate(prompt)

            if sources:

                answer += "\n\n---\n"
                answer += "### 📚 Sources\n"

                for source in sources:
                    answer += f"- {source}\n"

            return answer

        except Exception as e:

            print("RAG Agent Error:", e)

            return (
                "❌ An error occurred while searching the college knowledge base."
            )

    def run(self, state):
        """
        Called by the workflow.
        """

        if self.rag_tool:
            return self.rag_tool.process(state)

        query = state.get("query", "")

        return self.process(query)