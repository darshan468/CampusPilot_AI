import streamlit as st


def sidebar():

    # --------------------------
    # Logo
    # --------------------------
    st.sidebar.image(
        "https://img.icons8.com/color/96/graduation-cap.png",
        width=70
    )

    st.sidebar.title("🎓 CampusPilot AI")
    st.sidebar.caption("Agentic AI Powered Smart Campus")

    st.sidebar.divider()

    # --------------------------
    # Theme Toggle
    # --------------------------
    if "theme" not in st.session_state:
        st.session_state.theme = "Light"

    dark_mode = st.sidebar.toggle(
        "🌙 Dark Mode",
        value=(st.session_state.theme == "Dark")
    )

    st.session_state.theme = "Dark" if dark_mode else "Light"

    st.sidebar.divider()

    # --------------------------
    # Navigation
    # --------------------------
    menu = st.sidebar.radio(
        "📌 Navigation",
        [
            "🏠 Dashboard",
            "👤 Student Profile",
            "📚 Study Planner",
            "📝 Assignments",
            "📅 Timetable",
            "💼 Placement Hub",
            "🎯 Career Guide",
            "📢 Events",
            "🤖 AI Assistant"
        ]
    )

    # --------------------------
    # Footer
    # --------------------------
    st.sidebar.markdown("<br>" * 8, unsafe_allow_html=True)

    st.sidebar.divider()

    st.sidebar.markdown(
        "<h5 style='text-align:center;'>Developed By</h5>",
        unsafe_allow_html=True,
    )

    with st.sidebar.container(border=True):
        st.markdown(
            "<h4 style='text-align:center; color:#198754; margin:0;'>Darshan S</h4>",
            unsafe_allow_html=True,
        )

    return menu