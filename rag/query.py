from rag.retriever import CampusRetriever
from core.llm import llm


class RAGQuery:

    def __init__(self):

        self.retriever = CampusRetriever()

    def ask(self, question: str):

        context = self.retriever.retrieve_text(question)

        if not context:

            return (
                "I couldn't find relevant information "
                "in the college documents."
            )

        prompt = f"""
You are CampusPilot AI.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        return llm.generate(prompt)