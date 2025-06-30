import streamlit as st
from todo_manager import initialize_state, add_todo
from ui_components import todo_form, render_todo_item

st.title("Todo List App")

# 初期化
initialize_state()

# Todoリストの初期化
todo_form()
    
# Todoリストの表示
for i, todo in enumerate(st.session_state["todo_list"]):
    render_todo_item(i, todo)


