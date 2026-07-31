"""
==========================================================
CampusPilot AI
Career Service
==========================================================
Business logic for Career Guidance.
"""

from repositories.career_repository import CareerRepository


class CareerService:

    def __init__(self):

        self.repository = CareerRepository()

    # =====================================================
    # Generate Career Report
    # =====================================================

    def generate_report(
        self,
        target_role,
        current_skills,
        experience,
        career_goal,
        roadmap,
        recommendations
    ):

        career_data = {

            "target_role": target_role,

            "current_skills": current_skills,

            "experience": experience,

            "career_goal": career_goal,

            "roadmap": roadmap,

            "recommendations": recommendations

        }

        return self.repository.save(career_data)

    # =====================================================
    # Career History
    # =====================================================

    def get_history(self):

        return self.repository.get_all()

    # =====================================================
    # Latest Career Report
    # =====================================================

    def get_latest(self):

        return self.repository.get_latest()

    # =====================================================
    # Delete Career Report
    # =====================================================

    def delete_report(self, career_id):

        return self.repository.delete(career_id)

    # =====================================================
    # Total Reports
    # =====================================================

    def total_reports(self):

        return self.repository.total()