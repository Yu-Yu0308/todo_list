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
    edit_key = f"edit_mode_{i}"
    delete_key = f"delete_mode_{i}"
        
    if edit_key not in st.session_state:
        st.session_state[edit_key] = False  # 編集モードは初期状態ではオフ
    if delete_key not in st.session_state:
        st.session_state[delete_key] = False  # 削除モードは初期状態ではオフ

# Todoリストの表示と編集
for i, todo in enumerate(st.session_state["todo_list"]):
    edit_key = f"edit_mode_{i}"
    delete_key = f"delete_mode_{i}"
    
    with st.container():
        st.markdown("---")  # 区切り線
    
        # 編集モード：入力欄＋保存ボタン
        if st.session_state[edit_key]:
            new_todo = st.text_input(f"ToDo {i+1}", value=todo, key=f"edit_{i}")
            spacer, col1, col2 = st.columns([6, 1, 2])
            with col1:   
                if st.button("保存", key=f"save_btn_{i}"):
                    st.session_state["todo_list"][i] = new_todo
                    st.session_state[edit_key] = False # 編集モードOFF
            with col2:
                if st.button("キャンセル", key=f"cancel_btn_{i}"):
                    st.session_state[edit_key] = False  # 編集モードOFF
        
        # 削除モード：確認メッセージ＋削除ボタン
        elif st.session_state[delete_key]:
            st.write(f"本当に削除しますか？ 「{todo}」")
            col1, col2, spacer = st.columns([1, 1, 6]) 
            with col1:
                if st.button("はい", key=f"confirm_delete_btn_{i}"):
                    st.session_state["todo_list"].pop(i)
                    st.session_state[delete_key] = False
            with col2:
                if st.button("いいえ", key=f"cancel_delete_btn_{i}"):
                    st.session_state[delete_key] = False        
        
        # 通常モード：文字＋編集ボタン
        else:
            st.markdown(f"**ToDo {i+1}**")
            st.write(todo)
            # ボタンを右下に寄せるために空白列を作る
            spacer, col_edit, col_delete = st.columns([6, 1, 1])
            
            with col_edit:
                if st.button("編集", key=f"edit_btn_{i}"):
                    st.session_state[edit_key] = True # 編集モードON
            with col_delete:
                if st.button("削除", key=f"delete_btn_{i}"):
                    st.session_state[delete_key] = True  # 削除モードON

