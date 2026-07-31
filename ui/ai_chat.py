import streamlit as st

from graph.workflow import CampusPilotWorkflow
from memory.conversation_memory import ConversationMemory


def ai_chat_page():

    st.title("🎓 CampusPilot AI Copilot")
    st.caption("Your Multi-Agent AI Campus Assistant")

    st.divider()

    # -----------------------------------------
    # Session State
    # -----------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "memory" not in st.session_state:
        st.session_state.memory = ConversationMemory()

    if "workflow" not in st.session_state:
        st.session_state.workflow = CampusPilotWorkflow()

    workflow = st.session_state.workflow
    memory = st.session_state.memory

    # -----------------------------------------
    # Sidebar
    # -----------------------------------------

    with st.sidebar:

        st.subheader("💬 Conversation")

        if st.button("🗑 Clear Conversation"):

            st.session_state.messages = []

            memory.clear()

            st.success("Conversation cleared.")

            st.rerun()

    # -----------------------------------------
    # Display Previous Messages
    # -----------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # -----------------------------------------
    # Chat Input
    # -----------------------------------------

    prompt = st.chat_input("Ask CampusPilot AI anything...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        memory.add_message("user", prompt)

        with st.chat_message("user"):
            st.markdown(prompt)

        # -----------------------------------------
        # AI Response
        # -----------------------------------------

        with st.chat_message("assistant"):

            with st.spinner("🤖 CampusPilot AI is thinking..."):

                try:

                    response = workflow.run(
                        query=prompt,
                        memory=memory.get_context(),
                    )

                    if not response:
                        response = "⚠ No response generated."

                except Exception as e:

                    response = (
                        "❌ CampusPilot AI encountered an error.\n\n"
                        f"**{type(e).__name__}**\n\n{e}"
                    )

                st.markdown(response)

        memory.add_message("assistant", response)

        memory.set_last_query(prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )