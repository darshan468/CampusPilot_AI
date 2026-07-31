import streamlit as st

from database.database import db_manager


def recent_activity():

    st.subheader("🕒 Recent AI Activities")

    study = db_manager.get_total_study_plans()

    assignment = db_manager.get_total_assignments()

    if study > 0:

        st.success(f"📚 {study} Study Plan(s) Generated")

    if assignment > 0:

        st.success(f"📝 {assignment} Assignment(s) Created")

    if study == 0 and assignment == 0:

        st.info("No AI activities yet.")