import streamlit as st

st.title('my hogehoge') # タイトルの表示
st.header('This is a header') # ヘッダーの表示
st.subheader('This is a subheader') # サブヘッダー
st.text('Hello World!') # テキスト

# st.write()はMarkdown表記対応
st.write('# headline1')

input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)