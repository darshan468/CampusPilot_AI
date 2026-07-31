"""
==========================================================
CampusPilot AI Enterprise Workflow
==========================================================
Coordinates:

User
   ↓
Supervisor Agent
   ↓
Execution Engine
   ↓
Specialized Agents
   ↓
Merger Agent
   ↓
Final Response
==========================================================
"""

import time

from graph.state import AgentState

from agents.supervisor_agent import SupervisorAgent
from agents.merger_agent import MergerAgent

from core.container import ServiceContainer
from graph.execution_engine import ExecutionEngine


class CampusPilotWorkflow:

    def __init__(self):

        self.container = ServiceContainer()

        self.supervisor = SupervisorAgent()

        self.agent_manager = self.container.agent_manager

        self.execution_engine = ExecutionEngine(
            self.agent_manager
        )

    # =====================================================
    # Execute Workflow
    # =====================================================

    def run(
        self,
        query: str,
        memory: dict | None = None
    ) -> str:

        start_time = time.time()

        try:

            query = query.strip()

            if not query:

                return "Please enter a question."

            # ------------------------------------------------
            # Supervisor Routing
            # ------------------------------------------------

            decision = self.supervisor.process(query)

            if not isinstance(decision, dict):

                return (
                    "❌ Supervisor Agent returned "
                    "an invalid response."
                )

            agents = decision.get("agents", [])

            if not agents:

                return (
                    "❌ No suitable agent found."
                )

            execution_plan = decision.get(
                "execution_plan",
                []
            )

            if not execution_plan:

                execution_plan = [

                    {
                        "step": i + 1,
                        "agent": agent,
                        "status": "pending"
                    }

                    for i, agent in enumerate(agents)

                ]

            # ------------------------------------------------
            # Shared Agent State
            # ------------------------------------------------

            state: AgentState = {

                "query": query,

                "agents": agents,

                "execution_plan": execution_plan,

                "current_agent": "",

                "responses": [],

                "agent_results": {},

                "memory": memory or {},

                # Module Outputs
                "study_plan": None,
                "assignment_plan": None,
                "placement": None,
                "career_plan": None,
                "timetable": None,
                "rag_response": None,

                # Final
                "final_response": None,

                "error": None
            }

            # ------------------------------------------------
            # Execute Selected Agents
            # ------------------------------------------------

            state = self.execution_engine.execute_plan(state)

            if state is None:

                return (
                    "❌ Execution Engine "
                    "returned no state."
                )

            # ------------------------------------------------
            # Error Handling
            # ------------------------------------------------

            if state.get("error"):

                return (
                    "❌ Workflow Failed\n\n"
                    f"{state['error']}"
                )

            # ------------------------------------------------
            # Merge Responses
            # ------------------------------------------------

            responses = state.get(
                "responses",
                []
            )

            if responses:

                final_response = MergerAgent.merge(
                    responses
                )

            else:

                final_response = (
                    "⚠ No agent generated a response."
                )

            state["final_response"] = final_response

            elapsed = round(
                time.time() - start_time,
                2
            )

            print(
                f"[Workflow] Completed in "
                f"{elapsed} sec"
            )

            return final_response

        except Exception as e:

            return (
                "❌ CampusPilot Workflow Error\n\n"
                f"{type(e).__name__}: {e}"
            )