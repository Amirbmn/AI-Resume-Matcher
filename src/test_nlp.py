import streamlit as st

st.title("Streamlit Test")

st.write("Streamlit is working!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}!")