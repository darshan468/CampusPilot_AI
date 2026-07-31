import streamlit as st
from datetime import date

from database.database import db_manager
from agents.placement_agent import PlacementAgent


def placement_page():

    st.title("💼 AI Placement Hub")
    st.caption("Track your placements and receive AI-powered guidance.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        company = st.text_input("🏢 Company")

        role = st.text_input("💻 Job Role")

        interview_date = st.date_input(
            "📅 Interview Date",
            value=date.today()
        )

    with col2:

        status = st.selectbox(
            "📌 Application Status",
            [
                "Preparing",
                "Applied",
                "Interview",
                "Selected",
                "Rejected"
            ]
        )

        skills = st.text_input(
            "🛠 Required Skills",
            placeholder="Python, SQL, DSA, React..."
        )

    notes = st.text_area(
        "📝 Notes",
        placeholder="Interview rounds, preparation strategy, reminders..."
    )

    uploaded_resume = st.file_uploader(
        "📄 Upload Resume (Optional)",
        type=["pdf"]
    )

    st.divider()

    if st.button(
        "🚀 Save & Get AI Guidance",
        use_container_width=True
    ):

        try:

            db_manager.save_placement({

                "company": company,

                "role": role,

                "status": status,

                "interview_date": str(interview_date),

                "notes": notes

            })

        except Exception as e:

            st.warning(f"Database Error: {e}")

        placement_agent = PlacementAgent()

        with st.spinner("🤖 CampusPilot AI is preparing your placement guidance..."):

            guidance = placement_agent.generate_guidance(

                company=company,

                role=role,

                skills=skills,

                query=notes

            )

        st.success("✅ Placement information saved successfully!")

        st.markdown("## 🎯 AI Placement Guidance")

        st.markdown(guidance)

        if uploaded_resume is not None:

            st.info(
                "📄 Resume uploaded successfully.\n\n"
                "Resume analysis will be available in the next update."
            )