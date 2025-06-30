import streamlit as st
from todo_manager import remove_todo, update_todo, add_todo, clear_todo_state

def todo_form():
    with st.form(key="todo_form"):
        todo_input = st.text_input("新しいTodoを入力", key="input_todo")
        submitted = st.form_submit_button("追加", on_click = add_todo)
    
def render_todo_item(i, todo):
    edit_key = f"edit_mode_{i}"
    delete_key = f"delete_mode_{i}"
    done_key = f"done_mode_{i}"
    
    # 状態の初期化
    for key in [edit_key, delete_key, done_key]:
        if key not in st.session_state:
            st.session_state[key] = False
    
        
    with st.container():
        cols = st.columns([1, 5, 1, 1])
        st.markdown("---")  # 区切り線
        
        # 完了チェックボックス
        with cols[0]:
            st.checkbox("", value=st.session_state[done_key], key=done_key)
        
        with cols[1]:
            # 編集モード：入力欄＋保存ボタン
            if st.session_state[edit_key]:
                new_text = st.text_input(f"ToDo {i+1}", value=todo, key=f"edit_{i}")
                col1, col2 = st.columns([1, 1])
                with col1:   
                    if st.button("保存", key=f"save_btn_{i}"):
                        update_todo(i, new_text)
                        st.session_state[edit_key] = False # 編集モードOFF
                        st.rerun()
                with col2:
                    if st.button("キャンセル", key=f"cancel_btn_{i}"):
                        st.session_state[edit_key] = False  # 編集モードOFF
                        st.rerun()
            
            # 削除モード：確認メッセージ＋削除ボタン
            elif st.session_state[delete_key]:
                st.warning(f"「{todo}」を削除しますか？", icon="⚠️")
                col1, col2 = st.columns([1, 1]) 
                with col1:
                    if st.button("はい", key=f"confirm_delete_btn_{i}"):
                        remove_todo(i)
                        clear_todo_state()
                        st.rerun()
                with col2:
                    if st.button("いいえ", key=f"cancel_delete_btn_{i}"):
                        st.session_state[delete_key] = False
                        st.rerun()        
            
            # 通常モード：文字＋編集ボタン
            else:
                if st.session_state[done_key]:
                    st.markdown(f"~~ToDo {i+1}：{todo}~~")
                    st.markdown(f"~~{todo}~~")
                else:
                    st.markdown(f"**ToDo {i+1}**")
                    st.write(todo)

        with cols[2]:
            if not st.session_state[edit_key] and not st.session_state[delete_key]:
                if st.button("編集", key=f"edit_btn_{i}"):
                    st.session_state[edit_key] = True # 編集モードON
                    st.rerun()

        with cols[3]:
            if not st.session_state[edit_key] and not st.session_state[delete_key]:
                if st.button("削除", key=f"delete_btn_{i}"):
                    st.session_state[delete_key] = True  # 削除モードON
                    st.rerun()
