"""
==========================================================
CampusPilot AI
Event Agent
==========================================================
Handles all event-related operations by interacting
with EventTools.
"""

from tools.event_tools import EventTools


class EventAgent:

    def __init__(self):
        self.tools = EventTools()

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

        return self.tools.add_event(
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
        return self.tools.get_events()

    # =====================================================
    # Get Upcoming Events
    # =====================================================

    def get_upcoming_events(self):
        return self.tools.get_upcoming_events()

    # =====================================================
    # Get Latest Event
    # =====================================================

    def get_latest_event(self):
        return self.tools.get_latest_event()

    # =====================================================
    # Delete Event
    # =====================================================

    def delete_event(self, event_id):
        return self.tools.delete_event(event_id)

    # =====================================================
    # Total Events
    # =====================================================

    def total_events(self):
        return self.tools.total_events()