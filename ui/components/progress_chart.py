import streamlit as st
import plotly.express as px
import pandas as pd

from database.database import db_manager


def progress_chart():

    study = db_manager.get_total_study_plans()

    assignment = db_manager.get_total_assignments()

    pending = db_manager.get_pending_assignments()

    completed = db_manager.get_completed_assignments()

    df = pd.DataFrame({

        "Category": [

            "Study Plans",

            "Assignments",

            "Pending",

            "Completed"

        ],

        "Count": [

            study,

            assignment,

            pending,

            completed

        ]

    })

    fig = px.bar(

        df,

        x="Category",

        y="Count",

        text="Count",

        title="📊 CampusPilot AI Analytics"

    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True
    )