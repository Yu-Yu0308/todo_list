import streamlit as st

st.title("Todo List App")

# Todoリストの初期化
if "todo_list" not in st.session_state:
    st.session_state["todo_list"] = []

# 入力された内容をTodoリストに追加する関数
def add_todo():
    todo = st.session_state["input_todo"]
    if todo:  # 入力が空でない場合のみ追加
        st.session_state["todo_list"].append(todo)
        st.session_state["input_todo"] = ""  # 入力フィールドをクリア

with st.form(key='todo_form'):
    #リストに要素を追加
    st.text_input("Enter a new todo item", key="input_todo")
    add_button = st.form_submit_button('Add Todo', on_click=add_todo)  # ボタンが押されたときにadd_todo関数を呼び出す

# Todoリストの表示
for item in st.session_state["todo_list"]:
    st.write("・" + item)
    
