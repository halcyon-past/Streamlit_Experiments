import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="📚",
)

st.title("Projects")

st.write("You are", st.session_state["my_input"])