import streamlit as st

def initialize_state():
    if "todo_list" not in st.session_state:
        st.session_state["todo_list"] = []
        
def add_todo():
    todo_text = st.session_state.get("input_todo")
    if todo_text:
        st.session_state["todo_list"].append(todo_text)
        st.session_state["input_todo"] = ""  # 入力フィールドをクリア

def remove_todo(index):
    st.session_state["todo_list"].pop(index)

def update_todo(index, new_text):
    st.session_state["todo_list"][index] = new_text
    
def clear_todo_state():
    for key in list(st.session_state.keys()):
        if key.startswith("edit_mode_") or key.startswith("delete_mode_") or key.startswith("done_mode_"):
            del st.session_state[key]
