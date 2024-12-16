import streamlit as st

# アプリのタイトル
st.title('タスク管理アプリ')

# リストのデータを保存するためのセッションステート
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# タスクを追加するためのテキスト入力
new_task = st.text_input('新しいタスクを入力してください')

# タスク追加ボタン
if st.button('タスクを追加'):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f'タスク "{new_task}" が追加されました！')
    else:
        st.warning('タスクが空です。入力してください。')

# タスクの表示
if st.session_state.tasks:
    st.subheader('ToDoリスト:')
    for idx, task in enumerate(st.session_state.tasks, 1):
        st.write(f'{idx}. {task}')
else:
    st.write('現在、タスクはありません。')

# タスク削除ボタン（オプション）
delete_task = st.number_input('削除するタスクの番号を入力:', min_value=0, max_value=len(st.session_state.tasks), step=1)
if st.button('タスクを削除'):
    if delete_task and delete_task <= len(st.session_state.tasks):
        deleted_task = st.session_state.tasks.pop(delete_task - 1)
        st.success(f'タスク "{deleted_task}" が削除されました！')
    else:
        st.warning('削除するタスク番号が無効です。')
