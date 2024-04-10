import streamlit as st
import random 
import time

def response_generator():
    response=random.choice(
        [
            "Hello there! How can I assit you today?",
            "Hi, Human, need help?",
            "Do you need help or not?"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.5)

st.title("Chatbot with Streaming")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:=st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})

    with st.chat_message("assistant"):
        response=st.write_stream(response_generator)
    st.session_state.messages.append({'role':'assistant','content':response})

    

