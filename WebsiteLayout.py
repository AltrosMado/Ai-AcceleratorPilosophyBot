import streamlit as st

# page configuration
st.set_page_config(
    page_title="Website Blueprint",
    layout="wide",
    initial_sidebar_state="expanded"
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

# Page header
st.markdown('<header><h1>Normal Header</h1></header>', unsafe_allow_html=True)

# Main layout 
with st.container():
    col1, col2 = st.columns([3, 1])  # the column ratio

    # Main content (section)
    with col1:
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.subheader("Main Interaction Point")
        st.write("This is where the main content or interaction will occur.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar content (aside)
    with col2:
        st.markdown('<div class="sidebar">', unsafe_allow_html=True)
        st.subheader("Params for Bot")
        st.write("Place parameters or controls here for bot functionality.")
        st.markdown('</div>', unsafe_allow_html=True)


