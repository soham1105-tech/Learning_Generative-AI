from dotenv import load_dotenv
load_dotenv()

from langchain_openrouter import ChatOpenRouter
import streamlit as st
llm = ChatOpenRouter(model="dots-studio/dots-3-note-preview:free")

st.title("AI Chatbot")
st.markdown("My QnA Bot with LangChain and OpenRouter model...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything? ")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai","content":res.content})
