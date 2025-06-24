import streamlit as st

st.title("📝 テキスト入力アプリ")
user_input = st.text_area("テキストを入力してください:")
if user_input:
    st.write(f"入力されたテキスト: {user_input}")