import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My TODO App")
st.subheader("List of my todos")
st.write("random text")



for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new Item...",
              on_change=add_todo, key="new_todo")