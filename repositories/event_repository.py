"""
==========================================================
CampusPilot AI
Event Repository
==========================================================
Handles all database operations for Events.
"""

from database.database import db_manager


class EventRepository:

    def __init__(self):
        self.db = db_manager

    # =====================================================
    # Create Event
    # =====================================================

    def save(self, event_data):
        """
        Save a new event.
        """
        try:
            return self.db.save_event(event_data)
        except Exception as e:
            raise Exception(f"Failed to save event: {e}")

    # =====================================================
    # Get All Events
    # =====================================================

    def get_all(self):
        """
        Return all events.
        """
        try:
            return self.db.get_events()
        except Exception as e:
            raise Exception(f"Failed to fetch events: {e}")

    # =====================================================
    # Get Upcoming Events
    # =====================================================

    def get_upcoming(self):
        """
        Return upcoming events.
        """
        try:
            return self.db.get_upcoming_events()
        except Exception as e:
            raise Exception(f"Failed to fetch upcoming events: {e}")

    # =====================================================
    # Get Latest Event
    # =====================================================

    def get_latest(self):
        """
        Return the latest created event.
        """
        try:
            return self.db.get_latest_event()
        except Exception as e:
            raise Exception(f"Failed to fetch latest event: {e}")

    # =====================================================
    # Delete Event
    # =====================================================

    def delete(self, event_id):
        """
        Delete an event by ID.
        """
        try:
            return self.db.delete_event(event_id)
        except Exception as e:
            raise Exception(f"Failed to delete event: {e}")

    # =====================================================
    # Total Events
    # =====================================================

    def total(self):
        """
        Return total number of events.
        """
        try:
            return self.db.get_total_events()
        except Exception as e:
            raise Exception(f"Failed to count events: {e}")