import streamlit as st

st.title("My Personal Website")

# Create columns for navigation
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.write("Welcome to my homepage!")

with col2:
    if st.button("About Me"):
        st.write("This is the About Me page.")

with col3:
    if st.button("Projects"):
        st.write("Here are my projects.")

with col4:
    if st.button("Contact"):
        st.write("Contact information goes here.")