import streamlit as st
import requests

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

        # Initialize chat history if not already in session state
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
                # Add the user's message to chat history
                st.session_state.chat_history.append(("user", user_input))

                # Call the Flask API
                try:
                    api_url = "YOUR_NGROK_PUBLIC_URL/query"  # Replace with Flask app URL
                    response = requests.post(api_url, json={"question": user_input})
                    if response.status_code == 200:
                        bot_response = response.json().get("response", "No response received.")
                    else:
                        bot_response = f"Error: {response.json().get('error', 'Unknown error')}"
                except Exception as e:
                    bot_response = f"Error: {e}"

                # Add the bot's response to chat history
                st.session_state.chat_history.append(("bot", bot_response))
            else:
                st.error("Please enter a question before sending.")

        
        # Display chat history
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.write(f"**You:** {message}")
            else:
                st.write(f"**Philosophy Bot:** {message}")
        
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
