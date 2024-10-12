import streamlit as st

st.title("My Personal Website")

page = st.selectbox("Choose a page:", ["Home", "About Me", "Projects", "Contact"])

if page == "Home":
    st.write("Welcome to my homepage!")
elif page == "About Me":
    st.write("This is the About Me page.")
elif page == "Projects":
    st.write("Here are my projects.")
elif page == "Contact":
    st.write("Contact information goes here.")