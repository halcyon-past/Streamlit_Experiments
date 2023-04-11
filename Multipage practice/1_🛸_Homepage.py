import streamlit as st

st.set_page_config(
    page_title="Multipage",
    page_icon="🛸",
)

st.title("Main Page")
st.sidebar.success("Select a page above to get started.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Enter your name", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write("Hello", my_input)
