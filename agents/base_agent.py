from abc import ABC, abstractmethod
from graph.state import AgentState


class BaseAgent(ABC):
    """
    Base class for all CampusPilot AI agents.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def process(self, state: AgentState) -> AgentState:
        """
        Execute the agent logic.
        """
        pass

    # -------------------------------------------------
    # Hooks
    # -------------------------------------------------

    def before_execution(self, state: AgentState):

        print(f"[{self.name}] Started")

        return state

    def after_execution(self, state: AgentState):

        print(f"[{self.name}] Completed")

        return state

    # -------------------------------------------------
    # Error Handling
    # -------------------------------------------------

    def handle_error(
        self,
        state: AgentState,
        error: Exception
    ) -> AgentState:

        state["error"] = str(error)

        print(f"[{self.name}] Error : {error}")

        return state

    # -------------------------------------------------
    # Common Runner
    # -------------------------------------------------

    def run(self, state: AgentState) -> AgentState:

        try:

            self.before_execution(state)

            state = self.process(state)

            self.after_execution(state)

            return state

        except Exception as e:

            return self.handle_error(state, e)