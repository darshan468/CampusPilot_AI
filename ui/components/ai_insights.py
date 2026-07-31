import streamlit as st

from database.database import db_manager


def ai_insights():

    st.subheader("🤖 AI Insights")

    study = db_manager.get_total_study_plans()

    assignments = db_manager.get_total_assignments()

    pending = db_manager.get_pending_assignments()

    completed = db_manager.get_completed_assignments()

    student = db_manager.get_student()

    if student:

        st.info(
            f"🎯 Career Goal: {student.career_goal}"
        )

        st.info(
            f"📖 Preferred Study Time: {student.preferred_study_time}"
        )

    if study == 0:

        st.warning(
            "📚 You haven't created any study plans."
        )

    elif study < 5:

        st.info(
            "📚 Create more study plans for better preparation."
        )

    else:

        st.success(
            "🎉 Excellent study consistency!"
        )

    if pending > 0:

        st.warning(
            f"📝 Complete your {pending} pending assignment(s)."
        )

    if completed >= 5:

        st.success(
            "🏆 Outstanding assignment completion!"
        )

    if assignments == 0:

        st.info(
            "📝 Start managing assignments using CampusPilot AI."
        )