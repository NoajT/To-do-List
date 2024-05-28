import streamlit as st
import functions

tasks = functions.get_tasks()

st.title("My To-do List App")
st.write("This app is made to increase your productivity")


for task in tasks:
    st.checkbox(task)

st.text_input(label="XX",
              label_visibility='hidden',
              placeholder="Enter tasks here...")
