import streamlit as st

st.title("My Personal Website")

col1, col2 = st.columns(2)

with col1:
    if st.button("Home"):
        st.write("Welcome to my homepage!")

with col2:
    if st.button("About Me"):
        st.write("This is the About Me page.")

col3, col4 = st.columns(2)

with col3:
    if st.button("Projects"):
        st.write("Here are my projects.")

with col4:
    if st.button("Contact"):
        st.write("Contact information goes here.")