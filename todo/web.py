import streamlit as st
import functions

todos = functions.get_todos()

st.title("My TODO App")
st.subheader("List of my todos")
st.write("random text")



for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new Item...")