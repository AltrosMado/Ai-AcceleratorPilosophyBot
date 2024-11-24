import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Website Blueprint",
    layout="wide",
    initial_sidebar_state="collapsed"  # The sidebar 
)

# Styling 
st.markdown("""
    <style>
    /* Main styles */
    .main {
        background-color: #2d2d4f; /* Midnight Purple */
        color: #ffffff;
    }

    /* Header styling */
    header {
        background-color: #1e1e2f;
        color: #ffffff;
        padding: 1rem;
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
        border-bottom: 2px solid #333;
    }

    /* Section content */
    .content {
        background-color: #383850;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        margin-bottom: 1rem;
    }

    /* Sidebar content */
    .sidebar {
        background-color: #45456b;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Parameters set 
params = {
    "bot_name": "StreamlitBot",
    "model": "GPT-4",
    "theme": "Midnight Purple",
    "debug_mode": False
}

# Page header
st.markdown('<header><h1>Normal Header</h1></header>', unsafe_allow_html=True)

# Main layout 
with st.container():
    col1, col2 = st.columns([3, 1])  # The column ratio

    # Main content (section)
    with col1:
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.subheader("Main Interaction Point")
        st.write("""
            This is the central section where primary interaction will take place.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar content (aside)
    with col2:
        st.markdown('<div class="sidebar">', unsafe_allow_html=True)
        st.subheader("Info Panel")
        st.write(f"Bot Name: **{params['bot_name']}**")
        st.write(f"Model: **{params['model']}**")
        st.write(f"Theme: **{params['theme']}**")
        st.write(f"Debug Mode: **{'Enabled' if params['debug_mode'] else 'Disabled'}**")
        st.markdown('</div>', unsafe_allow_html=True)
