from repositories.event_repository import EventRepository


class EventService:

    def __init__(self):
        self.repository = EventRepository()

    def create_event(
        self,
        title,
        event_type,
        event_date,
        event_time,
        venue,
        organizer,
        description
    ):

        event_data = {
            "title": title,
            "event_type": event_type,
            "event_date": event_date,
            "event_time": event_time,
            "venue": venue,
            "organizer": organizer,
            "description": description
        }

        self.repository.save(event_data)

        return {
            "success": True,
            "message": "Event added successfully."
        }

    def get_events(self):
        return self.repository.get_all()

    def get_upcoming_events(self):
        return self.repository.get_upcoming()

    def get_latest_event(self):
        return self.repository.get_latest()

    def delete_event(self, event_id):
        return self.repository.delete(event_id)

    def total_events(self):
        return self.repository.total()