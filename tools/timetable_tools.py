"""
==========================================================
CampusPilot AI
Timetable Tool
==========================================================
Tool Layer for Timetable Agent
==========================================================
"""

from services.timetable_service import TimetableService


class TimetableTools:

    def __init__(self):
        self.service = TimetableService()

    # =====================================================
    # Add Class
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

        return self.service.create_timetable(
            day=day,
            subject=subject,
            faculty=faculty,
            start_time=start_time,
            end_time=end_time,
            room=room
        )

    # =====================================================
    # Get All Classes
    # =====================================================

    def get_all_classes(self):

        return self.service.get_all_classes()

    # =====================================================
    # Today's Classes
    # =====================================================

    def get_today_classes(self):

        return self.service.get_today_classes()

    # =====================================================
    # Update Class
    # =====================================================

    def update_class(
        self,
        timetable_id,
        updated_data
    ):

        return self.service.update_class(
            timetable_id,
            updated_data
        )

    # =====================================================
    # Delete Class
    # =====================================================

    def delete_class(self, timetable_id):

        return self.service.delete_class(timetable_id)

    # =====================================================
    # Statistics
    # =====================================================

    def total_classes(self):

        return self.service.total_classes()