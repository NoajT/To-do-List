import streamlit as st
import functions

tasks = functions.get_tasks()


def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)


st.title("My To-do List App")
st.write("This app is made to increase your productivity")


for task in tasks:
    st.checkbox(task)

st.text_input(label="XX", label_visibility='hidden',
              placeholder="Enter tasks here...",
              on_change=add_task, key="new_task")
