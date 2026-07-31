import streamlit as st
from datetime import date

from agents.event_agent import EventAgent


class EventPage:

    def __init__(self):
        self.agent = EventAgent()

    def render(self):

        st.title("🎉 Campus Events")

        tab1, tab2, tab3 = st.tabs([
            "➕ Add Event",
            "📋 All Events",
            "📅 Upcoming Events"
        ])

        # =====================================================
        # Add Event
        # =====================================================

        with tab1:

            st.subheader("Add New Event")

            title = st.text_input("Event Title")

            event_type = st.selectbox(
                "Event Type",
                [
                    "Workshop",
                    "Seminar",
                    "Hackathon",
                    "Placement Drive",
                    "Cultural Fest",
                    "Sports",
                    "Other"
                ]
            )

            event_date = st.date_input(
                "Event Date",
                value=date.today()
            )

            event_time = st.time_input("Event Time")

            venue = st.text_input("Venue")

            organizer = st.text_input("Organizer")

            description = st.text_area("Description")

            if st.button("Add Event", use_container_width=True):

                if title.strip() == "":
                    st.warning("Please enter event title.")
                    st.stop()

                try:

                    self.agent.add_event(
                        title,
                        event_type,
                        event_date,
                        str(event_time),
                        venue,
                        organizer,
                        description
                    )

                    st.success("✅ Event Added Successfully")

                except Exception as e:

                    st.error(str(e))

        # =====================================================
        # View All Events
        # =====================================================

        with tab2:

            st.subheader("All Campus Events")

            events = self.agent.get_events()

            if events:

                for event in events:

                    with st.expander(
                        f"{event.title} ({event.event_type})"
                    ):

                        st.write(f"📅 Date : {event.event_date}")
                        st.write(f"🕒 Time : {event.event_time}")
                        st.write(f"📍 Venue : {event.venue}")
                        st.write(f"👤 Organizer : {event.organizer}")
                        st.write(event.description)

                        if st.button(
                            "Delete",
                            key=f"delete_{event.id}"
                        ):

                            self.agent.delete_event(event.id)

                            st.success("Event Deleted")

                            st.rerun()

            else:

                st.info("No events available.")

        # =====================================================
        # Upcoming Events
        # =====================================================

        with tab3:

            st.subheader("Upcoming Events")

            events = self.agent.get_upcoming_events()

            if events:

                for event in events:

                    st.info(
                        f"🎯 {event.title}\n\n"
                        f"📅 {event.event_date}\n\n"
                        f"📍 {event.venue}"
                    )

            else:

                st.warning("No upcoming events.")