import streamlit as st
from datetime import datetime

from memory.student_memory import StudentMemory


def dashboard_header():

    # -----------------------------
    # Greeting
    # -----------------------------
    current_time = datetime.now()
    hour = current_time.hour

    if hour < 12:
        greeting = "Good Morning ☀️"
    elif hour < 17:
        greeting = "Good Afternoon 🌤️"
    else:
        greeting = "Good Evening 🌙"

    # -----------------------------
    # Student Profile
    # -----------------------------
    student = StudentMemory.get_profile()

    st.title("🎓 CampusPilot AI")
    st.caption(greeting)

    if student:

        # Welcome text (without green success box)
        st.markdown(f"### Welcome back, **{student.name}** 👋")

        st.markdown(
            f"""
**Department:** {student.department} &nbsp;&nbsp; | &nbsp;&nbsp;
**Year:** {student.year} &nbsp;&nbsp; | &nbsp;&nbsp;
**Semester:** {student.semester}
""",
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "⚠ Please complete your Student Profile to unlock personalized recommendations."
        )

    # -----------------------------
    # Today's Date
    # -----------------------------
    st.caption(
        f"📅 Today : {current_time.strftime('%A, %d %B %Y')}"
    )