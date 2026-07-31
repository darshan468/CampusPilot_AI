"""
==========================================================
CampusPilot AI
Career Repository
==========================================================
Handles all database operations for Career Guidance.
"""

from database.database import db_manager


class CareerRepository:

    def __init__(self):
        self.db = db_manager

    # =====================================================
    # Save Career Report
    # =====================================================

    def save(self, career_data):

        return self.db.save_career(career_data)

    # =====================================================
    # Get All Career Reports
    # =====================================================

    def get_all(self):

        return self.db.get_careers()

    # =====================================================
    # Get Latest Career Report
    # =====================================================

    def get_latest(self):

        return self.db.get_latest_career()

    # =====================================================
    # Delete Career Report
    # =====================================================

    def delete(self, career_id):

        return self.db.delete_career(career_id)

    # =====================================================
    # Total Reports
    # =====================================================

    def total(self):

        return self.db.get_total_career_reports()