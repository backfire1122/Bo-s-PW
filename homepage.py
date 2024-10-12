import streamlit as st

st.title("My Personal Website")

with st.expander("Home"):
    st.write("Welcome to my homepage!")

with st.expander("About Me"):
    st.write("This is the About Me page.")

with st.expander("Projects"):
    st.write("Here are my projects.")

with st.expander("Contact"):
    st.write("Contact information goes here.")