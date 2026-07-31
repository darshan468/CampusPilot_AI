"""
==========================================================
CampusPilot AI
Timetable Service
==========================================================
Business Logic Layer for Timetable
==========================================================
"""

from repositories.timetable_repository import TimetableRepository


class TimetableService:

    def __init__(self):
        self.repository = TimetableRepository()

    # =====================================================
    # Create Timetable
    # =====================================================

    def create_timetable(
        self,
        day,
        subject,
        faculty,
        start_time,
        end_time,
        room
    ):

        timetable_data = {
            "day": day,
            "subject": subject,
            "faculty": faculty,
            "start_time": start_time,
            "end_time": end_time,
            "room": room
        }

        return self.repository.save(timetable_data)

    # =====================================================
    # Get All Timetable
    # =====================================================

    def get_all_classes(self):

        return self.repository.get_all()

    # =====================================================
    # Get Today's Timetable
    # =====================================================

    def get_today_classes(self):

        return self.repository.get_today()

    # =====================================================
    # Update Timetable
    # =====================================================

    def update_class(self, timetable_id, updated_data):

        return self.repository.update(
            timetable_id,
            updated_data
        )

    # =====================================================
    # Delete Timetable
    # =====================================================

    def delete_class(self, timetable_id):

        return self.repository.delete(timetable_id)

    # =====================================================
    # Total Classes
    # =====================================================

    def total_classes(self):

        return self.repository.total_classes()