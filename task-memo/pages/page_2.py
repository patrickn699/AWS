import streamlit as st



st.title("memo items")



def memos_data(inserted):

    if inserted:

        task = st.text_input("Enter your task name")
        description = st.text_input("Enter your task description")
        status = st.text_input("Enter your task status")
        priority = st.text_input("Enter your task priority")
        due_date = st.date_input("Enter your task due date")
        created_date = st.date_input("Enter your task created date")
        updated_date = st.date_input("Enter your task updated date")

        if st.button("Create") and task and description and status and priority and due_date and created_date and updated_date:
            op = memo.create_memo(task, description, status, priority, due_date, created_date, updated_date)
            st.success(op)

        else:
            st.error("Please enter all the fields")

    else:
        st.error("Please sign in")


def show_wid(ya):
    if ya:
        memos_data(True)