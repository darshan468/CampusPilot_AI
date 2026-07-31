import streamlit as st
from datetime import datetime

from agents.timetable_agent import TimetableAgent


class TimetablePage:

    def __init__(self):
        self.agent = TimetableAgent()

    def render(self):

        st.title("📅 Timetable Management")

        tab1, tab2, tab3 = st.tabs(
            [
                "➕ Add Class",
                "📖 View Timetable",
                "📅 Today's Classes"
            ]
        )

        # =====================================================
        # Add Class
        # =====================================================

        with tab1:

            st.subheader("Add New Class")

            day = st.selectbox(
                "Day",
                [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"
                ]
            )

            subject = st.text_input("Subject")

            faculty = st.text_input("Faculty")

            col1, col2 = st.columns(2)

            with col1:
                start_time = st.text_input(
                    "Start Time",
                    placeholder="09:00 AM"
                )

            with col2:
                end_time = st.text_input(
                    "End Time",
                    placeholder="10:00 AM"
                )

            room = st.text_input("Room")

            if st.button("Add Class", width="stretch"):

                if not subject.strip():

                    st.warning("Please enter the subject.")
                    st.stop()

                try:

                    self.agent.add_class(
                        day,
                        subject,
                        faculty,
                        start_time,
                        end_time,
                        room
                    )

                    st.success("Class added successfully.")

                except Exception as e:

                    st.error(str(e))

        # =====================================================
        # View Timetable
        # =====================================================

        with tab2:

            st.subheader("Complete Timetable")

            timetable = self.agent.get_timetable()

            if timetable:

                for item in timetable:

                    with st.expander(
                        f"{item.day} | {item.subject}"
                    ):

                        st.write(f"**Faculty:** {item.faculty}")
                        st.write(
                            f"**Time:** {item.start_time} - {item.end_time}"
                        )
                        st.write(f"**Room:** {item.room}")

                        if st.button(
                            "🗑 Delete",
                            key=f"delete_{item.id}"
                        ):

                            self.agent.delete_class(item.id)

                            st.success("Class deleted successfully.")

                            st.rerun()

            else:

                st.info("No timetable found.")

        # =====================================================
        # Today's Classes
        # =====================================================

        with tab3:

            today = datetime.today().strftime("%A")

            st.subheader(f"Today's Classes ({today})")

            try:

                timetable = self.agent.get_timetable()

                today_classes = [
                    item
                    for item in timetable
                    if item.day == today
                ]

                if today_classes:

                    for item in today_classes:

                        st.info(
                            f"🕒 {item.start_time} - {item.end_time}\n\n"
                            f"📘 {item.subject}\n\n"
                            f"👨‍🏫 {item.faculty}\n\n"
                            f"🏫 {item.room}"
                        )

                else:

                    st.warning("No classes scheduled for today.")

            except Exception as e:

                st.error(str(e))