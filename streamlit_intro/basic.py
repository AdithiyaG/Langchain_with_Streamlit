import streamlit as st

with st.chat_message("user"):
    st.write("Hello")
assistant=st.chat_message("assistant")
assistant.write("Hola Motherfucker")

#chat_input
prompt=st.chat_input("Fuck you")
if prompt:
    st.write(f"User has sent the following : {prompt}")