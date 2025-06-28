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

# 入力欄
with st.form(key='todo_form'):
    #リストに要素を追加
    st.text_input("新しいToDoを入力", key="input_todo")
    add_button = st.form_submit_button('追加', on_click=add_todo)  # ボタンが押されたときにadd_todo関数を呼び出す

# 編集モードの状態を管理(ToDoごとに)
for i in range(len(st.session_state["todo_list"])):
    key = f"edit_mode_{i}"
    if key not in st.session_state:
        st.session_state[key] = False  # 編集モードは初期状態ではオフ

# Todoリストの表示と編集
for i, todo in enumerate(st.session_state["todo_list"]):
    edit_key = f"edit_mode_{i}"
    
    # 編集モード：入力欄＋保存ボタン
    if st.session_state[edit_key]:
        new_todo = st.text_input(f"ToDo {i+1}", value=todo, key=f"edit_{i}")
        if st.button("保存", key=f"save_btn_{i}"):
            st.session_state["todo_list"][i] = new_todo
            st.session_state[edit_key] = False # 編集モードOFF
        if st.button("キャンセル", key=f"cancel_btn_{i}"):
            st.session_state[edit_key] = False  # 編集モードOFF
    
    # 通常モード：文字＋編集ボタン
    else:
        st.write(f"・{todo}")
        if st.button("編集", key=f"edit_btn_{i}"):
            st.session_state[edit_key] = True # 編集モードON
            

