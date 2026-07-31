import streamlit as st

from database.database import db_manager


def recommendations():

    st.subheader("🤖 AI Recommendations")

    pending = db_manager.get_pending_assignments()

    study_plans = db_manager.get_total_study_plans()

    completed = db_manager.get_completed_assignments()

    if study_plans == 0:

        st.warning("📚 Create your first AI Study Plan.")

    elif study_plans < 3:

        st.info("📖 Generate more study plans for better preparation.")

    if pending > 0:

        st.warning(
            f"📝 You have {pending} pending assignment(s)."
        )

    if completed >= 5:

        st.success(
            "🎉 Excellent! Keep maintaining your progress."
        )

    if pending == 0 and study_plans > 0:

        st.success(
            "🚀 Great! You are on track."
        )