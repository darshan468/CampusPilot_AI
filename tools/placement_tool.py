from core.prompts import Prompts


class PlacementTool:
    """
    ==========================================================
    CampusPilot AI - Placement Tool
    ==========================================================

    Responsibilities
    ----------------
    • Generate AI placement guidance
    • Save placement information
    """

    def __init__(self, repository, llm):

        self.repository = repository
        self.llm = llm

    def placement_guidance(
        self,
        company,
        role,
        skills,
        query=""
    ):
        """
        Generate AI placement preparation guidance.
        """

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

1. Explain the interview process.
2. List important technical topics.
3. Suggest aptitude preparation.
4. Suggest coding practice.
5. Suggest resume improvements.
6. Recommend useful projects.
7. Give interview tips.
8. Return the response in Markdown.
"""

        response = self.llm.generate(prompt)

        try:

            self.repository.save_placement({

                "company": company,

                "role": role,

                "skills": skills,

                "notes": query

            })

        except Exception:
            # Ignore database save errors
            pass

        return response

    def process(self, state):
        """
        Called by PlacementAgent.
        """

        return self.placement_guidance(

            company=state.get("company", ""),

            role=state.get("role", ""),

            skills=state.get("skills", ""),

            query=state.get("query", "")

        )