import streamlit as st

from database.database import db_manager


def show():

    st.title("📅 Timetable Manager")

    st.divider()

    with st.form("timetable_form"):

        col1, col2 = st.columns(2)

        with col1:

            day = st.selectbox(
                "Day",
                [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday"
                ]
            )

            subject = st.text_input("Subject")

            faculty = st.text_input("Faculty")

        with col2:

            start_time = st.time_input("Start Time")

            end_time = st.time_input("End Time")

            room = st.text_input("Room")

        submit = st.form_submit_button("➕ Add Class")

    if submit:

        if not subject:

            st.error("Please enter subject name.")

        else:

            db_manager.save_timetable(

                {
                    "day": day,
                    "subject": subject,
                    "faculty": faculty,
                    "start_time": str(start_time),
                    "end_time": str(end_time),
                    "room": room
                }

            )

            st.success("Class added successfully.")

    st.divider()

    st.subheader("Weekly Timetable")

    timetable = db_manager.get_timetable()

    if timetable:

        for row in timetable:

            st.container(border=True)

            st.markdown(
                f"""
### 📘 {row.subject}

**Day:** {row.day}

**Time:** {row.start_time} - {row.end_time}

**Faculty:** {row.faculty}

**Room:** {row.room}
"""
            )

    else:

        st.info("No classes added yet.")