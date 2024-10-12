import streamlit as st

# Set the title of the app
st.title("Welcome to My Personal Website!")

# Create an upper navigation bar using a selectbox
page = st.selectbox("Navigate", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.write("""
    Thank you for stopping by! It's been quite a journey to create this space where I can share a bit about myself.
    While I may not have much to offer beyond the everyday adventures of my life, I hope you find something relatable or inspiring here.
    Join me as I navigate through the ups and downs, the mundane and the exciting—welcome to my world!
    """)

# About Me Page
elif page == "About Me":
    st.write("""
    This is the About Me page where I share my background, interests, and journey.
    I am passionate about [Your Interests], and I enjoy [Your Hobbies].
    """)

# Projects Page
elif page == "Projects":
    st.write("""
    Here are some of the projects I've worked on:
    - Project 1: Description
    - Project 2: Description
    - Project 3: Description
    """)

# Contact Page
elif page == "Contact":
    st.write("""
    Feel free to reach out to me at [Your Email] or connect with me on [Your Social Media].
    """)

# Optional: Add a footer or additional info
st.markdown("### Connect with Me")
st.write("Links to your social media or any additional information can go here.")