import streamlit as st
from datetime import date

from database.database import db_manager
from agents.assignment_agent import AssignmentAgent


def assignment_page():

    st.title("📝 AI Assignment Planner")
    st.caption("Manage assignments with AI-powered planning")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        subject = st.text_input("📚 Subject")

        assignment_title = st.text_input("📝 Assignment Title")

    with col2:

        due_date = st.date_input(
            "📅 Due Date",
            min_value=date.today()
        )

        priority = st.selectbox(
            "🔥 Priority",
            [
                "High",
                "Medium",
                "Low"
            ]
        )

    st.divider()

    if st.button(
        "🚀 Generate Assignment Plan",
        use_container_width=True,
        disabled=(
            subject.strip() == "" or
            assignment_title.strip() == ""
        )
    ):

        assignment_agent = AssignmentAgent()

        with st.spinner("🤖 CampusPilot AI is preparing your assignment plan..."):

            plan = assignment_agent.generate_assignment_plan(
                subject=subject,
                assignment_title=assignment_title,
                due_date=due_date,
                priority=priority
            )

        try:

            db_manager.save_assignment({

                "subject": subject,
                "assignment_title": assignment_title,
                "due_date": due_date,
                "priority": priority,
                "ai_plan": plan

            })

        except Exception as e:

            st.warning(f"Database Error: {e}")

        st.success("✅ Assignment Plan Generated Successfully!")

        st.markdown("## 📝 Your AI Assignment Plan")

        st.markdown(plan)