import json

from core.llm import llm
from graph.state import AgentState
from agents.base_agent import BaseAgent


class SupervisorAgent(BaseAgent):
    """
    CampusPilot AI Supervisor Agent

    Responsibilities
    ----------------
    • Understand the user's intent
    • Select the correct AI agent(s)
    • Build an execution plan
    """

    VALID_AGENTS = [
        "study",
        "assignment",
        "timetable",
        "placement",
        "career",
        "events",
        "rag",
        "chat"
    ]

    def __init__(self):
        super().__init__("Supervisor Agent")

    # =====================================================
    # Process
    # =====================================================

    def process(self, state: AgentState) -> AgentState:

        query = state.get("query", "")

        prompt = f"""
You are the Supervisor Agent of CampusPilot AI.

Your task is to determine which AI agent(s) should handle the user's request.

Available Agents

study
- Study plans
- Revision plans
- Exam preparation
- Learning schedules

assignment
- Assignment planning
- Homework
- Academic projects

timetable
- Timetable
- Class schedules
- Daily schedule
- Today's classes

placement
- Resume
- Placement
- Interviews
- Career preparation

career
- Career guidance
- Higher studies
- Skill roadmap

events
- College events
- Workshops
- Seminars
- Hackathons

rag
- College rules
- Attendance
- Hostel
- Library
- Regulations
- Syllabus
- Academic information

chat
- General conversation
- Greetings
- Questions outside the above categories

Rules

1. Return ONLY JSON.
2. Never explain.
3. Use only valid agent names.
4. Multiple agents are allowed.
5. If unsure return ["rag"].

Return exactly:

{{
    "agents":["study"],
    "reason":"short reason",
    "confidence":0.95
}}

User Query

{query}
"""

        try:

            response = llm.generate(prompt)

            content = response.strip()

            # Remove markdown fences
            if content.startswith("```"):

                lines = content.splitlines()

                content = "\n".join(
                    line
                    for line in lines
                    if not line.startswith("```")
                )

            result = json.loads(content)

            agents = result.get("agents", [])

            # Remove duplicates
            agents = list(dict.fromkeys(agents))

            # Keep only valid agents
            agents = [
                agent
                for agent in agents
                if agent in self.VALID_AGENTS
            ]

            if not agents:
                agents = ["rag"]

            execution_plan = []

            for index, agent in enumerate(agents):

                execution_plan.append(
                    {
                        "step": index + 1,
                        "agent": agent,
                        "status": "pending"
                    }
                )

            state["agents"] = agents

            state["execution_plan"] = execution_plan

            state["reason"] = result.get(
                "reason",
                "No reason provided."
            )

            state["confidence"] = result.get(
                "confidence",
                0.80
            )

            return state

        except Exception as e:

            return self.handle_error(state, e)