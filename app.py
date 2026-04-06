import streamlit as st
from chatbot import ask_question
import time

st.set_page_config(page_title="EV Diagnostic Assistant", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Settings")

model = st.sidebar.selectbox(
    "Select Model",
    ["qwen:0.5b", "tinyllama"]
)

top_k = st.sidebar.slider("Top-K Retrieval", 1, 5, 1)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

st.title("⚡ EV Diagnostic Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask about EV manuals..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner("Analyzing manuals..."):
            response, sources = ask_question(
                prompt,
                model=model,
                top_k=top_k,
                temperature=temperature
            )

        full_response = response
        message_placeholder.markdown(full_response)

        if sources:
            with st.expander("📚 Sources"):
                for s in sources:
                    st.write(f"- {s}")

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )