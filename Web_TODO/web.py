import streamlit as st
import functions
#streamlit run web.py

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""




st.title("My Dates")
st.subheader("This is My Appointments.")
st.write("This app is to remind me.")


for index, todo in enumerate(todos):

    test2 = f"({index}) {todo}"
    #st.warning(test2)
    #checkbox = st.checkbox(todo, key=todo)
    checkbox = st.checkbox(test2, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        #st.experimental_rerun()
        st.rerun()

st.text_input(label="-", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')