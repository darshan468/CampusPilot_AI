"""
==========================================================
CampusPilot AI
Event Tools
==========================================================
Acts as the bridge between the Event Agent and
the Event Service.
"""

from services.event_service import EventService


class EventTools:

    def __init__(self):
        self.service = EventService()

    # =====================================================
    # Add Event
    # =====================================================

    def add_event(
        self,
        title,
        event_type,
        event_date,
        event_time,
        venue,
        organizer,
        description
    ):
        return self.service.create_event(
            title,
            event_type,
            event_date,
            event_time,
            venue,
            organizer,
            description
        )

    # =====================================================
    # Get All Events
    # =====================================================

    def get_events(self):
        return self.service.get_events()

    # =====================================================
    # Get Upcoming Events
    # =====================================================

    def get_upcoming_events(self):
        return self.service.get_upcoming_events()

    # =====================================================
    # Get Latest Event
    # =====================================================

    def get_latest_event(self):
        return self.service.get_latest_event()

    # =====================================================
    # Delete Event
    # =====================================================

    def delete_event(self, event_id):
        return self.service.delete_event(event_id)

    # =====================================================
    # Total Events
    # =====================================================

    def total_events(self):
        return self.service.total_events()