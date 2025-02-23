import streamlit as st
# app title 
st.title("Task Planner App")
# installation of session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []
# sidebar heading
st.sidebar.header("Organize your Task")

#text input
new_task = st.sidebar.text_input("Add a New Task:", placeholder="Enter your Task here...")

if st.sidebar.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed":False})
        st.success("Task Successfully Added!")
    else:
        st.warning("Task cannot be empty!")

#display tasks
st.subheader("Your Task List")
if not st.session_state.tasks:
    st.info("No tasks yet! Add one from the sidebar to get started.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1 , col2 , col3 = st.columns([0.7,0.15,0.15])

        #mark as completed
        completed = col1.checkbox(f"{task['task']}",task["completed"],key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        #update task
        if col2.button("edit",key=f"edit_{index}"):
          new_task = st.text_input("edit task",task["task"],key=f'edit_{index}')
          if new_task and st.button("save", key=f'save_{index}'):
              st.session_state.tasks[index]["task"] = new_task
              st.experimental_rerun()
        # delete task
        if col3.button("Delete",key=f'delete_{index}'):
            del st.session_state.tasks[index]
            st.experimental_rerun()

        #clear all tasks
if st.button("Remove All Tasks"):
            st.session_state.tasks = []
            st.success("All tasks removed successfully")

        #footer
st.markdown('---')
st.caption("Boost your productivity with this simple To-Do List App!")
