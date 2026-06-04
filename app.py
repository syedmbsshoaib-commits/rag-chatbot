import streamlit as st
from chat import chat
from embeddings import chunk_text, find_relevant_chunks

@st.cache_resource
def load_knowledge_base():
    with open("documents/faq.txt", "r") as f:
        text = f.read()
    return chunk_text(text)

chunks = load_knowledge_base()

st.title("TechCorp Support Chatbot")
st.caption("Powered by Claude + RAG")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask a question..."):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    relevant_chunks = find_relevant_chunks(prompt, chunks)
    context = "\n\n".join(relevant_chunks)
    reply = chat(st.session_state.conversation, prompt, context=context)

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})