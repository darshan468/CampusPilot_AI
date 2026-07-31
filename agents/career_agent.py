"""
==========================================================
CampusPilot AI
Career Agent
==========================================================
Handles all Career Guidance requests.
"""

from agents.base_agent import BaseAgent
from graph.state import AgentState
from tools.career_tool import CareerTool


class CareerAgent(BaseAgent):

    def __init__(self):

        super().__init__("Career Agent")

        self.tool = CareerTool()

    # =====================================================
    # Process Request
    # =====================================================

    def process(self, state: AgentState) -> AgentState:

        try:

            action = state.get("action", "generate")

            # ------------------------------------------
            # Generate Career Report
            # ------------------------------------------

            if action == "generate":

                student = state.get("student", {})

                report = self.tool.generate_career_report(

                    target_role=student.get(
                        "target_role",
                        "Software Engineer"
                    ),

                    current_skills=student.get(
                        "skills",
                        "Python"
                    ),

                    experience=student.get(
                        "experience",
                        "Fresher"
                    ),

                    career_goal=student.get(
                        "career_goal",
                        "Product Based Company"
                    )
                )

                state["career_plan"] = report

                state["result"] = report

                state.setdefault("responses", []).append(report)

            # ------------------------------------------
            # Career History
            # ------------------------------------------

            elif action == "history":

                history = self.tool.get_history()

                state["result"] = history

            # ------------------------------------------
            # Latest Report
            # ------------------------------------------

            elif action == "latest":

                latest = self.tool.get_latest()

                state["result"] = latest

            # ------------------------------------------
            # Statistics
            # ------------------------------------------

            elif action == "stats":

                total = self.tool.total_reports()

                state["result"] = {
                    "total_reports": total
                }

            else:

                state["error"] = (
                    f"Unsupported action: {action}"
                )

        except Exception as e:

            state["error"] = (
                f"Career Agent Error: {e}"
            )

        return state