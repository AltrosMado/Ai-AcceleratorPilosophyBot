import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Philosophy Tutor Chatbot",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Styling
st.markdown(
    """
    <style>
    body {
        background-color: #2d2d4f; /* Midnight Purple */
        color: #ffffff;
    }

    .main {
        background-color: #2d2d4f;
        color: #ffffff;
    }

    .content {
        background-color: #383850;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        margin-bottom: 1rem;
    }

    .sidebar {
        background-color: #45456b;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }

    .chat-container {
        background-color: #1e1e2f;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<h1 style='text-align: center;'>Philosophy Chatbot Tutor</h1>", unsafe_allow_html=True)

# Layout
with st.container():
    col1, col2 = st.columns([3, 1])  # Main content and sidebar

    # Main Content
    with col1:
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.subheader("Chat with the Philosophy Tutor")
        st.write(
            """
            Welcome to the Philosophy Tutor chatbot! Use the text box below to ask your questions about philosophy,
            explore complex ideas, and learn in an interactive way.
            """
        )

        # Chatbox
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Display chat history
        for message in st.session_state.chat_history:
            role, content = message
            if role == "user":
                st.write(f"**You:** {content}")
            else:
                st.write(f"**Philosophy Bot:** {content}")

        # Input Box
        user_input = st.text_input("Your Question:", key="user_input")
        if st.button("Send"):
            if user_input.strip():
                st.session_state.chat_history.append(("user", user_input))
                # Placeholder for bot response
                st.session_state.chat_history.append(("bot", "Response from the Philosophy Bot will appear here."))
            else:
                st.error("Please enter a question before sending.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar
    with col2:
        st.markdown('<div class="sidebar">', unsafe_allow_html=True)
        st.subheader("Info Panel")
        st.write("Project: AI-Powered Philosophy Tutor")
        st.write("Version: 1.0")
        st.write("Developer: Team 24")
        st.write("Status: Ready")
        st.markdown('</div>', unsafe_allow_html=True)

