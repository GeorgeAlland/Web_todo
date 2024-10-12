import streamlit as st
import functions
#del st.session_state[todo]

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""




st.title("My Day")
st.subheader("Things to do today")
st.write("(Reminders and tasks)")


for index, todo in enumerate(todos):

    test2 = f"({index}) {todo}"

    #st.warning(test2)
    #checkbox = st.checkbox(todo, key=todo)
    #checkbox = st.checkbox(test2, key=todo)
    checkbox = st.checkbox(test2, key=test2)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        #del st.session_state[todo]
        del st.session_state[test2]
        #st.experimental_rerun()
        st.rerun()

st.text_input(label="-", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')