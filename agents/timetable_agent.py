"""
==========================================================
CampusPilot AI
Timetable Agent
==========================================================
Handles timetable-related operations.
==========================================================
"""

from agents.base_agent import BaseAgent
from graph.state import AgentState
from tools.timetable_tools import TimetableTools


class TimetableAgent(BaseAgent):

    def __init__(self):
        super().__init__("Timetable Agent")
        self.tools = TimetableTools()

    # =====================================================
    # Main Workflow Entry
    # =====================================================

    def process(self, state: AgentState) -> AgentState:

        action = state.get("action")

        try:

            if action == "add":

                result = self.tools.add_class(
                    day=state.get("day"),
                    subject=state.get("subject"),
                    faculty=state.get("faculty"),
                    start_time=state.get("start_time"),
                    end_time=state.get("end_time"),
                    room=state.get("room")
                )

            elif action == "list":

                result = self.tools.get_all_classes()

            elif action == "today":

                result = self.tools.get_today_classes()

            elif action == "update":

                result = self.tools.update_class(
                    timetable_id=state.get("timetable_id"),
                    updated_data=state.get("updated_data")
                )

            elif action == "delete":

                result = self.tools.delete_class(
                    timetable_id=state.get("timetable_id")
                )

            elif action == "stats":

                result = self.tools.total_classes()

            else:

                raise ValueError(
                    f"Unknown timetable action: {action}"
                )

            state["result"] = result
            state["status"] = "success"

            if "responses" not in state:
                state["responses"] = {}

            state["responses"]["timetable"] = result

            return state

        except Exception as e:

            return self.handle_error(state, e)

    # =====================================================
    # Streamlit UI Methods
    # =====================================================

    def add_class(
        self,
        day,
        subject,
        faculty,
        start_time,
        end_time,
        room
    ):

        return self.tools.add_class(
            day,
            subject,
            faculty,
            start_time,
            end_time,
            room
        )

    def get_timetable(self):

        return self.tools.get_all_classes()

    def get_today_timetable(self):

        return self.tools.get_today_classes()

    def update_class(
        self,
        timetable_id,
        updated_data
    ):

        return self.tools.update_class(
            timetable_id,
            updated_data
        )

    def delete_class(
        self,
        timetable_id
    ):

        return self.tools.delete_class(
            timetable_id
        )

    def total_classes(self):

        return self.tools.total_classes()