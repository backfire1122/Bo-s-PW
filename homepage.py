import streamlit as st

import streamlit as st

st.title("My Personal Website")

# Create navigation buttons
if st.button("Home"):
    st.write("Welcome to my homepage!")
elif st.button("About Me"):
    st.write("This is the About Me page.")
elif st.button("Projects"):
    st.write("Here are my projects.")
elif st.button("Contact"):
    st.write("Contact information goes here.")