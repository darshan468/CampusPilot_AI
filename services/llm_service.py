from core.llm import llm


class LLMService:
    """
    ==========================================================
    CampusPilot AI - LLM Service
    ==========================================================

    Responsibilities
    ----------------
    • Provide a common interface to the LLM
    • Generate AI responses
    • Invoke the underlying model
    """

    def __init__(self):
        self.llm = llm

    def generate(self, prompt: str) -> str:
        """
        Generate a plain text response.
        """
        try:
            return self.llm.generate(prompt)
        except Exception as e:
            raise RuntimeError(f"LLM generation failed: {e}")

    def invoke(self, prompt: str):
        """
        Return the raw LLM response object.
        """
        try:
            return self.llm.invoke(prompt)
        except Exception as e:
            raise RuntimeError(f"LLM invocation failed: {e}")