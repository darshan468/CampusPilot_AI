import streamlit as st

from database.database import db_manager


def dashboard_cards():

    # -----------------------------
    # Fetch Dashboard Data
    # -----------------------------

    total_study_plans = db_manager.get_total_study_plans()

    total_assignments = db_manager.get_total_assignments()

    pending_assignments = db_manager.get_pending_assignments()

    completed_assignments = db_manager.get_completed_assignments()

    # -----------------------------
    # KPI Cards
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="📚 Study Plans",
            value=total_study_plans
        )

    with col2:

        st.metric(
            label="📝 Assignments",
            value=total_assignments
        )

    with col3:

        st.metric(
            label="⏳ Pending",
            value=pending_assignments
        )

    with col4:

        st.metric(
            label="✅ Completed",
            value=completed_assignments
        )