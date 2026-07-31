import streamlit as st
from datetime import date

from database.database import db_manager
from agents.study_agent import StudyAgent


def study_page():

    st.title("📚 AI Study Planner")
    st.caption("Create a personalized AI study plan")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        subject = st.text_input("📚 Subject")

        exam_date = st.date_input(
            "📅 Exam Date",
            min_value=date.today()
        )

    with col2:

        daily_hours = st.selectbox(
            "⏰ Daily Study Hours",
            [
                "1 Hour",
                "2 Hours",
                "3 Hours",
                "4 Hours",
                "5+ Hours"
            ]
        )

        difficulty = st.selectbox(
            "📈 Difficulty Level",
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        )

    st.divider()

    if not subject:
        st.info("Enter the subject to generate a study plan.")

    if st.button(
        "🚀 Generate Study Plan",
        use_container_width=True,
        disabled=(subject.strip() == "")
    ):

        with st.spinner("🤖 CampusPilot AI is generating your study plan..."):

            study_agent = StudyAgent()

            plan = study_agent.generate_study_plan(
                subject=subject,
                exam_date=exam_date,
                daily_hours=daily_hours,
                difficulty=difficulty
            )

        try:

            db_manager.save_study_plan(
                {
                    "subject": subject,
                    "exam_date": exam_date,
                    "daily_hours": daily_hours,
                    "difficulty": difficulty,
                    "plan": plan
                }
            )

        except Exception as e:

            st.warning(f"Database Error: {e}")

        st.success("✅ Study Plan Generated Successfully!")

        st.markdown("## 📚 Your Personalized Study Plan")

        st.markdown(plan)