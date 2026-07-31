"""
==========================================================
CampusPilot AI
Career Guidance Page
==========================================================
"""

import streamlit as st

from agents.career_agent import CareerAgent


class CareerPage:

    def __init__(self):

        self.agent = CareerAgent()

    def render(self):

        st.title("🎯 AI Career Guidance")

        st.markdown(
            "Generate a personalized AI-powered career roadmap."
        )

        st.divider()

        # =====================================================
        # Career Form
        # =====================================================

        with st.form("career_form"):

            target_role = st.selectbox(
                "🎯 Target Role",
                [
                    "Software Engineer",
                    "Data Analyst",
                    "Data Scientist",
                    "Machine Learning Engineer",
                    "AI Engineer",
                    "Full Stack Developer",
                    "Backend Developer",
                    "Frontend Developer",
                    "Cloud Engineer",
                    "Cyber Security Engineer"
                ]
            )

            current_skills = st.text_area(
                "💻 Current Skills",
                placeholder="Python, SQL, FastAPI, React..."
            )

            experience = st.selectbox(
                "👨‍💻 Experience",
                [
                    "Fresher",
                    "Intern",
                    "0-1 Years",
                    "1-3 Years",
                    "3+ Years"
                ]
            )

            career_goal = st.text_area(
                "🚀 Career Goal",
                placeholder="Describe your career objective..."
            )

            generate = st.form_submit_button(
                "🚀 Generate Career Roadmap"
            )

        # =====================================================
        # Generate Report
        # =====================================================

        if generate:

            if not current_skills.strip():

                st.warning("Please enter your current skills.")

                return

            with st.spinner("Generating AI Career Report..."):

                state = {

                    "action": "generate",

                    "student": {

                        "target_role": target_role,

                        "skills": current_skills,

                        "experience": experience,

                        "career_goal": career_goal

                    },

                    "responses": []

                }

                result = self.agent.run(state)

            if result.get("error"):

                st.error(result["error"])

            else:

                st.success("Career roadmap generated successfully!")

                st.markdown("## 📄 Career Report")

                st.markdown(result["career_plan"])

        st.divider()

        # =====================================================
        # Career Statistics
        # =====================================================

        st.subheader("📊 Career Statistics")

        stats_state = {

            "action": "stats",

            "responses": []

        }

        stats = self.agent.run(stats_state)

        total = 0

        if stats.get("result"):

            total = stats["result"].get(
                "total_reports",
                0
            )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Generated Reports",
                total
            )

        with col2:

            st.metric(
                "Target Role",
                target_role if 'target_role' in locals() else "-"
            )

        st.divider()

        # =====================================================
        # Latest Career Report
        # =====================================================

        st.subheader("📝 Latest Career Report")

        latest_state = {

            "action": "latest",

            "responses": []

        }

        latest = self.agent.run(latest_state)

        report = latest.get("result")

        if report:

            st.write(f"**Target Role:** {report.target_role}")
            st.write(f"**Experience:** {report.experience}")

            with st.expander("View Career Roadmap"):

                st.markdown(report.roadmap)

        else:

            st.info("No career reports available.")

        st.divider()

        # =====================================================
        # Career History
        # =====================================================

        st.subheader("📚 Career History")

        history_state = {

            "action": "history",

            "responses": []

        }

        history = self.agent.run(history_state)

        reports = history.get("result")

        if reports:

            for report in reports:

                with st.expander(
                    f"{report.target_role} • {report.created_at.strftime('%d-%m-%Y %H:%M')}"
                ):

                    st.write(
                        f"**Experience:** {report.experience}"
                    )

                    st.write(
                        f"**Skills:** {report.current_skills}"
                    )

                    st.markdown(report.roadmap)

        else:

            st.info("No previous reports found.")