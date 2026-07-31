"""
==========================================================
CampusPilot AI
Execution Engine
==========================================================

Responsibilities
----------------
• Execute agents sequentially
• Update execution status
• Store agent outputs
• Handle runtime errors
• Stop execution if an agent fails
"""

import time

from graph.state import AgentState


class ExecutionEngine:

    def __init__(self, agent_manager):

        self.agent_manager = agent_manager

    # =====================================================
    # Execute Workflow
    # =====================================================

    def execute_plan(
        self,
        state: AgentState
    ) -> AgentState:

        execution_plan = state.get("execution_plan", [])

        if not execution_plan:

            state["error"] = "No execution plan found."
            return state

        state.setdefault("responses", [])
        state.setdefault("agent_results", {})

        for step in execution_plan:

            agent_name = step.get("agent")

            if not agent_name:

                step["status"] = "failed"

                state["error"] = (
                    "Execution plan contains an invalid agent."
                )

                break

            try:

                state["current_agent"] = agent_name

                step["status"] = "running"

                step["started_at"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                # ------------------------------------------
                # Get Agent
                # ------------------------------------------

                agent = self.agent_manager.get_agent(
                    agent_name
                )

                if agent is None:

                    raise ValueError(
                        f"Agent '{agent_name}' not registered."
                    )

                # ------------------------------------------
                # Execute Agent
                # ------------------------------------------

                state = agent.run(state)

                if state is None:

                    raise RuntimeError(
                        f"{agent_name} returned None."
                    )

                if state.get("error"):

                    step["status"] = "failed"

                    break

                # ------------------------------------------
                # Store Agent Result
                # ------------------------------------------

                result = state.get("result")

                if result is not None:

                    state["agent_results"][agent_name] = result

                    state["responses"].append(str(result))

                step["status"] = "completed"

                step["completed_at"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

            except Exception as e:

                step["status"] = "failed"

                step["completed_at"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                state["error"] = (
                    f"{agent_name} failed.\n\n"
                    f"{type(e).__name__}: {e}"
                )

                break

        return state