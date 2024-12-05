import streamlit as st
import requests

# Set up Streamlit
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
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<h1 style='text-align: center;'>Philosophy Chatbot Tutor</h1>", unsafe_allow_html=True)

# Chatbox logic
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input Box
user_input = st.text_input("Your Question:", key="user_input")
if st.button("Send"):
    if user_input.strip():
        # Add user input to the chat history
        st.session_state.chat_history.append(("user", user_input))

        # Call the Flask API
        try:
            api_url = "YOUR_NGROK_PUBLIC_URL/query"  # Replace with your Flask app URL
            response = requests.post(api_url, json={"question": user_input})
            if response.status_code == 200:
                bot_response = response.json().get("response", "No response received.")
            else:
                bot_response = f"Error: {response.json().get('error', 'Unknown error')}"
        except Exception as e:
            bot_response = f"Error: {e}"

        # Add bot response to the chat history
        st.session_state.chat_history.append(("bot", bot_response))
    else:
        st.error("Please enter a question before sending.")

# Display chat history
for role, message in st.session_state.chat_history:
    if role == "user":
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Philosophy Bot:** {message}")
