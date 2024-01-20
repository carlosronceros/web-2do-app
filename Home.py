import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("<i>This app is to increase your <b>productivity</b></i>.",
         unsafe_allow_html=True)  # html is only allowed in the write method.

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


# st.session_state  # used to debug and see input and changes when we check the box.

# Create a requirements.txt file by `pip freeze > requirements.txt`

# Project to deploy the app to a service provider.
