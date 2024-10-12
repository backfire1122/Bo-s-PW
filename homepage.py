import streamlit as st

st.title("Vicky Bo Peng")

# Create tabs
tabs = st.tabs(["Home", "About Me", "Projects", "Contact"])

with tabs[0]:
    st.write("Welcome to my homepage!")

with tabs[1]:
    st.write("This is the About Me page.")

with tabs[2]:
    st.write("Here are my projects.")

with tabs[3]:
    st.write("Contact information goes here.")