import streamlit as st


def load_theme():

    # ----------------------------
    # Default Theme
    # ----------------------------
    if "theme" not in st.session_state:
        st.session_state.theme = "Light"

    # ----------------------------
    # Light Theme
    # ----------------------------
    if st.session_state.theme == "Light":

        css = """
        <style>

        /* Main App */
        .stApp{
            background:#F8FAFC;
            color:#111827;
        }

        /* Main Container */
        .block-container{
            padding-top:1rem;
            padding-bottom:1rem;
        }

        /* Sidebar */
        section[data-testid="stSidebar"]{
            background:#FFFFFF;
            border-right:1px solid #E5E7EB;
        }

        /* Metric Cards */
        div[data-testid="stMetric"]{
            background:white;
            border:1px solid #E5E7EB;
            border-radius:12px;
            padding:15px;
        }

        /* Buttons */
        .stButton>button{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:10px;
        }

        .stButton>button:hover{
            background:#1D4ED8;
        }

        /* Input Fields */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div{
            border-radius:8px;
        }

        /* Hide Streamlit Footer */
        footer{
            visibility:hidden;
        }

        </style>
        """

    # ----------------------------
    # Dark Theme
    # ----------------------------
    else:

        css = """
        <style>

        /* Main App */
        .stApp{
            background:#0F172A;
            color:#F9FAFB;
        }

        /* Main Container */
        .block-container{
            padding-top:1rem;
            padding-bottom:1rem;
        }

        /* Sidebar */
        section[data-testid="stSidebar"]{
            background:#111827;
            border-right:1px solid #374151;
        }

        /* Metric Cards */
        div[data-testid="stMetric"]{
            background:#1F2937;
            border:1px solid #374151;
            border-radius:12px;
            padding:15px;
            color:white;
        }

        /* Buttons */
        .stButton>button{
            background:#22C55E;
            color:white;
            border:none;
            border-radius:10px;
        }

        .stButton>button:hover{
            background:#16A34A;
        }

        /* Inputs */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div{
            background:#1F2937 !important;
            color:white !important;
            border:1px solid #4B5563 !important;
            border-radius:8px;
        }

        /* Hide Streamlit Footer */
        footer{
            visibility:hidden;
        }

        </style>
        """

    st.markdown(css, unsafe_allow_html=True)