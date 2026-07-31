import streamlit as st

from database.database import db_manager

# ===========================
# UI Pages
# ===========================

from ui.dashboard import dashboard
from ui.profile import profile_page
from ui.study import study_page
from ui.assignment import assignment_page
from ui.placement import placement_page
from ui.ai_chat import ai_chat_page
from ui.career_page import CareerPage
from ui.timetable_page import TimetablePage
from ui.event_page import EventPage

# ===========================
# Components
# ===========================

from ui.components.sidebar import sidebar
from ui.components.theme import load_theme

# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="CampusPilot AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# Initialize Database
# ===========================

db_manager

# ===========================
# Initialize Theme
# ===========================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# ===========================
# Sidebar Navigation
# ===========================

menu = sidebar()

# ===========================
# Apply Selected Theme
# ===========================

load_theme()

# ===========================
# Navigation
# ===========================

if menu == "🏠 Dashboard":

    dashboard()

elif menu == "👤 Student Profile":

    profile_page()

elif menu == "📚 Study Planner":

    study_page()

elif menu == "📝 Assignments":

    assignment_page()

elif menu == "📅 Timetable":

    timetable = TimetablePage()
    timetable.render()

elif menu == "💼 Placement Hub":

    placement_page()

elif menu == "🎯 Career Guide":

    career = CareerPage()
    career.render()

elif menu == "📢 Events":

    events = EventPage()
    events.render()

elif menu == "🤖 AI Assistant":

    ai_chat_page()

else:

    st.error("Page not found.")