"""
==========================================================
CampusPilot AI
Career Tool
==========================================================
Acts as a bridge between the Career Agent and Career Service.
"""

from services.career_service import CareerService
from core.llm import llm


class CareerTool:

    def __init__(self):

        self.service = CareerService()

    # =====================================================
    # Generate AI Career Report
    # =====================================================

    def generate_career_report(
        self,
        target_role: str,
        current_skills: str,
        experience: str,
        career_goal: str
    ):

        prompt = f"""
You are an expert Career Guidance AI.

Generate a personalized career report.

Target Role:
{target_role}

Current Skills:
{current_skills}

Experience:
{experience}

Career Goal:
{career_goal}

Generate the report in this format:

1. Career Readiness Score (0-100)

2. Strengths

3. Skill Gaps

4. Learning Roadmap

5. Recommended Projects

6. Interview Preparation Tips

7. Recommended Certifications

8. Recommended Companies

Keep the response clear, structured, and practical.
"""

        response = llm.invoke(prompt)

        report = (
            response.content
            if hasattr(response, "content")
            else str(response)
        )

        self.service.generate_report(
            target_role=target_role,
            current_skills=current_skills,
            experience=experience,
            career_goal=career_goal,
            roadmap=report,
            recommendations=report
        )

        return report

    # =====================================================
    # Career History
    # =====================================================

    def get_history(self):

        return self.service.get_history()

    # =====================================================
    # Latest Career Report
    # =====================================================

    def get_latest(self):

        return self.service.get_latest()

    # =====================================================
    # Delete Career Report
    # =====================================================

    def delete_report(self, career_id):

        return self.service.delete_report(career_id)

    # =====================================================
    # Statistics
    # =====================================================

    def total_reports(self):

        return self.service.total_reports()