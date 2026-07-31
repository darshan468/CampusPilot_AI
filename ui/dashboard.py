import streamlit as st

from ui.components.dashboard_header import dashboard_header
from ui.components.dashboard_cards import dashboard_cards
from ui.components.recommendations import recommendations
from ui.components.upcoming_schedule import upcoming_schedule
from ui.components.progress_chart import progress_chart
from ui.components.recent_activity import recent_activity
from ui.components.ai_insights import ai_insights


def dashboard():

    # -----------------------------
    # Dashboard Header
    # -----------------------------
    dashboard_header()

    st.divider()

    # -----------------------------
    # KPI Cards
    # -----------------------------
    dashboard_cards()

    st.divider()

    # -----------------------------
    # AI Recommendations & Schedule
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        recommendations()

    with col2:
        upcoming_schedule()

    st.divider()

    # -----------------------------
    # Weekly Progress
    # -----------------------------
    progress_chart()

    st.divider()

    # -----------------------------
    # AI Insights
    # -----------------------------
    ai_insights()

    st.divider()

    # -----------------------------
    # Recent AI Activities
    # -----------------------------
    recent_activity()