"""
==========================================================
CampusPilot AI
Timetable Repository
==========================================================
Repository Layer
Handles all database operations for Timetable.
==========================================================
"""

from services.database_service import DatabaseService


class TimetableRepository:

    def __init__(self):
        self.database = DatabaseService()

    # =====================================================
    # Save Timetable
    # =====================================================

    def save(self, timetable_data):

        return self.database.save_timetable(
            timetable_data
        )

    # =====================================================
    # Get All Classes
    # =====================================================

    def get_all(self):

        return self.database.get_timetable()

    # =====================================================
    # Get Today's Classes
    # =====================================================

    def get_today(self):

        return self.database.get_today_timetable()

    # =====================================================
    # Update Class
    # =====================================================

    def update(
        self,
        timetable_id,
        updated_data
    ):

        return self.database.update_timetable(
            timetable_id,
            updated_data
        )

    # =====================================================
    # Delete Class
    # =====================================================

    def delete(
        self,
        timetable_id
    ):

        return self.database.delete_timetable(
            timetable_id
        )

    # =====================================================
    # Total Classes
    # =====================================================

    def total_classes(self):

        return self.database.get_total_classes()