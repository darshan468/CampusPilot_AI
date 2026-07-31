from graph.state import AgentState

from agents.study_agent import generate_study_plan
from agents.assignment_agent import generate_assignment_plan
from agents.rag_agent import RAGAgent
from agents.parser_agent import ParserAgent


class AgentExecutor:
    """
    CampusPilot AI Agent Executor

    Executes the selected agent and updates the shared AgentState.
    """

    @staticmethod
    def execute(state: AgentState) -> AgentState:

        agent = state.get("current_agent", "")
        query = state.get("query", "")
        memory = state.get("memory", {})

        if "responses" not in state:
            state["responses"] = []

        try:

            # =====================================================
            # STUDY AGENT
            # =====================================================
            if agent == "study":

                details = ParserAgent.extract_study_details(query)

                details = {**memory, **details}

                required = [
                    "subject",
                    "exam_date",
                    "daily_hours",
                    "difficulty"
                ]

                missing = [
                    field
                    for field in required
                    if not details.get(field)
                ]

                if missing:

                    response = (
                        "📚 **Study Planner**\n\n"
                        "Please provide:\n\n"
                        + "\n".join(
                            f"• {field.replace('_', ' ').title()}"
                            for field in missing
                        )
                    )

                else:

                    response = generate_study_plan(
                        subject=details["subject"],
                        exam_date=details["exam_date"],
                        daily_hours=details["daily_hours"],
                        difficulty=details["difficulty"]
                    )

                    state["study_plan"] = response
                    state["memory"] = details

            # =====================================================
            # ASSIGNMENT AGENT
            # =====================================================
            elif agent == "assignment":

                details = ParserAgent.extract_assignment_details(query)

                details = {**memory, **details}

                required = [
                    "subject",
                    "assignment_title",
                    "due_date",
                    "priority"
                ]

                missing = [
                    field
                    for field in required
                    if not details.get(field)
                ]

                if missing:

                    response = (
                        "📝 **Assignment Planner**\n\n"
                        "Please provide:\n\n"
                        + "\n".join(
                            f"• {field.replace('_', ' ').title()}"
                            for field in missing
                        )
                    )

                else:

                    response = generate_assignment_plan(
                        subject=details["subject"],
                        assignment_title=details["assignment_title"],
                        due_date=details["due_date"],
                        priority=details["priority"]
                    )

                    state["assignment_plan"] = response
                    state["memory"] = details

            # =====================================================
            # RAG AGENT
            # =====================================================
            elif agent == "rag":

                response = RAGAgent.process(query)

                state["rag_response"] = response

            # =====================================================
            # CAREER AGENT
            # =====================================================
            elif agent == "career":

                response = (
                    "🎯 Career Guidance Agent is under development."
                )

                state["career_plan"] = response

            # =====================================================
            # PLACEMENT AGENT
            # =====================================================
            elif agent == "placement":

                response = (
                    "💼 Placement Agent is under development."
                )

                state["placement"] = response

            # =====================================================
            # TIMETABLE AGENT
            # =====================================================
            elif agent == "timetable":

                response = (
                    "📅 Timetable Agent is under development."
                )

                state["timetable"] = response

            # =====================================================
            # EVENT AGENT
            # =====================================================
            elif agent == "event":

                response = (
                    "📢 Event Agent is under development."
                )

            # =====================================================
            # UNKNOWN AGENT
            # =====================================================
            else:

                response = (
                    f"❌ Unknown agent: {agent}"
                )

            state["responses"].append(response)

            return state

        except Exception as e:

            error_message = (
                f"❌ {agent.title()} Agent Error\n\n{str(e)}"
            )

            state["error"] = str(e)

            state["responses"].append(error_message)

            return state