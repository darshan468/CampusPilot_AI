import os

from langchain_groq import ChatGroq

from core.settings import (
    GROQ_API_KEY,
    MODEL_NAME,
)


class LLM:
    """
    ==========================================================
    CampusPilot AI - Central LLM Wrapper
    ==========================================================

    Features
    --------
    • Single shared LLM instance
    • Error handling
    • Health checking
    • Plain text responses
    • Legacy compatibility
    """

    def __init__(self):

        if not GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is missing. Check your .env file."
            )

        self.model = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0.3,
        )

    # ======================================================
    # Raw Response
    # ======================================================

    def invoke(self, prompt: str):

        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        try:

            return self.model.invoke(prompt)

        except Exception as e:

            raise RuntimeError(
                f"LLM invocation failed:\n{e}"
            )

    # ======================================================
    # Plain Text Response
    # ======================================================

    def generate(self, prompt: str) -> str:

        try:

            response = self.invoke(prompt)

            if response is None:
                return "No response generated."

            if hasattr(response, "content"):

                return str(response.content).strip()

            return str(response).strip()

        except Exception as e:

            return f"❌ LLM Error\n\n{e}"

    # ======================================================
    # Callable
    # ======================================================

    def __call__(self, prompt: str):

        return self.generate(prompt)

    # ======================================================
    # Health Check
    # ======================================================

    def health_check(self):

        try:

            response = self.model.invoke("Reply with only: OK")

            return {
                "status": "healthy",
                "message": response.content
            }

        except Exception as e:

            return {
                "status": "failed",
                "message": str(e)
            }

    # ======================================================
    # Connection Test
    # ======================================================

    def test_connection(self):

        try:

            response = self.model.invoke("Hello")

            return True

        except Exception:

            return False


# ==========================================================
# Singleton
# ==========================================================

llm = LLM()


# ==========================================================
# Compatibility
# ==========================================================

def generate_response(prompt: str):

    return llm.generate(prompt)