from graph.state import AgentState


class AgentManager:
    """
    ==========================================================
    CampusPilot AI - Agent Manager
    ==========================================================

    Responsibilities
    ----------------
    • Register agents
    • Retrieve agents
    • Execute agents
    • Handle execution errors
    """

    def __init__(self):

        self._agents = {}

    def register(self, name: str, agent):

        self._agents[name] = agent

    def register_many(self, agents: dict):

        self._agents.update(agents)

    def get(self, name: str):

        return self._agents.get(name)

    def available_agents(self):

        return list(self._agents.keys())

    def execute(self, state: AgentState) -> AgentState:

        agent_name = state.get("current_agent")

        if not agent_name:

            state["error"] = "No current agent specified."

            return state

        agent = self.get(agent_name)

        if agent is None:

            state["error"] = (
                f"Agent '{agent_name}' not found."
            )

            return state

        try:

            result = agent.run(state)

            # If agent returns a dictionary, merge it into state
            if isinstance(result, dict):

                state.update(result)

            # If agent returns a string, store it
            elif isinstance(result, str):

                state.setdefault("responses", []).append(result)

                state.setdefault("agent_results", {})[
                    agent_name
                ] = result

            return state

        except Exception as e:

            state["error"] = (
                f"{agent_name} execution failed:\n\n{str(e)}"
            )

            return state