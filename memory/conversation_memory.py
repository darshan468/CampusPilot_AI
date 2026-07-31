from typing import Dict, Any, List


class ConversationMemory:
    """
    ==========================================================
    CampusPilot AI Conversation Memory
    ==========================================================

    Stores

    • Chat History
    • Extracted Details
    • Previous Agent
    • Last User Query
    """

    def __init__(self):

        self.data = {
            "history": [],
            "context": {},
            "last_agent": None,
            "last_query": None
        }

    # ----------------------------------------------

    def add_message(
        self,
        role: str,
        content: str
    ):

        self.data["history"].append(
            {
                "role": role,
                "content": content
            }
        )

    # ----------------------------------------------

    def update_context(
        self,
        values: Dict[str, Any]
    ):

        if values:
            self.data["context"].update(values)

    # ----------------------------------------------

    def get_context(self):

        return self.data["context"]

    # ----------------------------------------------

    def set_last_agent(
        self,
        agent: str
    ):

        self.data["last_agent"] = agent

    # ----------------------------------------------

    def get_last_agent(self):

        return self.data["last_agent"]

    # ----------------------------------------------

    def set_last_query(
        self,
        query: str
    ):

        self.data["last_query"] = query

    # ----------------------------------------------

    def get_last_query(self):

        return self.data["last_query"]

    # ----------------------------------------------

    def get_history(self):

        return self.data["history"]

    # ----------------------------------------------

    def clear(self):

        self.data = {
            "history": [],
            "context": {},
            "last_agent": None,
            "last_query": None
        }