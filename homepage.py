import streamlit as st

# Set the title of the app
st.set_page_config(page_title="My Personal Website", layout="wide")

# Create a navigation bar
st.markdown("<h1 style='text-align: center;'>My Personal Website</h1>", unsafe_allow_html=True)

# Create a horizontal navigation bar
nav_items = ["Home", "About Me", "Projects", "Contact"]

# Create a row of buttons for navigation
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col1:
    if st.button("Home"):
        st.session_state.page = "Home"

with col2:
    if st.button("About Me"):
        st.session_state.page = "About Me"

with col3:
    if st.button("Projects"):
        st.session_state.page = "Projects"

with col4:
    if st.button("Contact"):
        st.session_state.page = "Contact"

# Set the default page
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Display content based on the selected page
if st.session_state.page == "Home":
    st.write("""
    Thank you for stopping by! It's been quite a journey to create this space where I can share a bit about myself.
    While I may not have much to offer beyond the everyday adventures of my life, I hope you find something relatable or inspiring here.
    Join me as I navigate through the ups and downs, the mundane and the exciting—welcome to my world!
    """)

elif st.session_state.page == "About Me":
    import about

elif st.session_state.page == "Projects":
    import projects

elif st.session_state.page == "Contact":
    import contact