from core.llm import llm
from core.prompts import Prompts


class PlacementAgent:
    """
    CampusPilot AI Placement Agent

    Responsibilities
    ----------------
    • Provide placement guidance
    • Generate interview preparation tips
    • Suggest technical skills
    • Help with resume improvement
    """

    def __init__(self, placement_tool=None):
        self.placement_tool = placement_tool

    def generate_guidance(
        self,
        company="",
        role="",
        skills="",
        query=""
    ):

        prompt = f"""
{Prompts.PLACEMENT}

Company:
{company}

Role:
{role}

Skills:
{skills}

Student Query:
{query}

Instructions:

1. Give placement preparation guidance.
2. Suggest important technical skills.
3. Recommend interview preparation topics.
4. Suggest aptitude and coding practice.
5. Recommend resume improvements.
6. Keep the response clear and structured.
7. Format the response using Markdown.
"""

        try:

            return llm.generate(prompt)

        except Exception as e:

            return f"""
## ❌ CampusPilot AI Error

Unable to generate placement guidance.

Reason:

{str(e)}
"""

    def run(self, state):
        """
        Called by the workflow.
        """

        if self.placement_tool:
            return self.placement_tool.placement_guidance(state)

        return self.generate_guidance(
            company=state.get("company", ""),
            role=state.get("role", ""),
            skills=state.get("skills", ""),
            query=state.get("query", "")
        )