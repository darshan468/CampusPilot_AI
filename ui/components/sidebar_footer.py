import streamlit as st


def sidebar_footer():

    st.sidebar.divider()

    # Add space so the footer appears near the bottom
    for _ in range(10):
        st.sidebar.empty()

    with st.sidebar.container(border=True):
        st.markdown(
            "<h5 style='text-align:center;margin-bottom:8px;'>Developed By</h5>",
            unsafe_allow_html=True,
        )

        st.success("Darshan S")