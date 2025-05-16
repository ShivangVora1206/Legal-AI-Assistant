import streamlit as st
import random, time
from rag_engine import query_legal_index

st.title("Legal RAG Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.02)

# React to user input
if prompt := st.chat_input("Ask a legal question..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Query the RAG engine
    response = query_legal_index(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        streamed = st.write_stream(response_generator(response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
