import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain.prompts import (PromptTemplate,
SystemMessagePromptTemplate,
HumanMessagePromptTemplate,
ChatPromptTemplate)
from langchain_core.output_parsers import StrOutputParser


st.title("ChatGPT Clone")

chat=AzureChatOpenAI(
    azure_deployment="gpt-4-32k",
    openai_api_version="2023-07-01-preview")

chatbot_template_str="""You are a Helpful Assitant who answer the query given the Human"""
review_system_prompt=SystemMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["context"],template=chatbot_template_str)
)
review_human_prompt=HumanMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["question"],template="{question}")
)

prompt_template=ChatPromptTemplate(input_variables=["question"],messages=[review_system_prompt,review_human_prompt])
output_parser = StrOutputParser()
chain=prompt_template | chat | output_parser



if 'deployment_name' not in st.session_state:
    st.session_state.deployment_name='gpt-4-32k'
if 'openai_api_version' not in st.session_state:
    st.session_state.openai_api_version="2023-07-01-preview"


if 'messages' not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:=st.chat_input("What can I do for you?"):
    st.session_state.messages.append({'role':'user','content':prompt})
    with st.chat_message('user'):
        st.write(prompt)
    with st.chat_message('assistant'):
        response=st.write_stream(chain.stream({'question':prompt}))
    st.session_state.messages.append({'role':'assistant','content':response})

        
        
    



