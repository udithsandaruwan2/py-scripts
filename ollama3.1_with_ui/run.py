import streamlit as st
import requests

# Streamlit setup
st.set_page_config(page_title="Chat with LLaMA 3.1", layout="centered")
st.title("🦙 Chat with LLaMA 3.1 (8B) via Ollama")

# Session state for storing messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful, concise assistant and a python developer."}
    ]

# Show chat history
for msg in st.session_state.messages[1:]:  # skip system
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your question here...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Build full prompt string
    full_prompt = ""
    for msg in st.session_state.messages:
        if msg["role"] == "system":
            full_prompt += f"<|system|>{msg['content']}<|end|>\n"
        elif msg["role"] == "user":
            full_prompt += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            full_prompt += f"AI: {msg['content']}\n"
    full_prompt += "AI:"

    # Send request to Ollama
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1",
                "prompt": full_prompt,
                "stream": False,
                "temperature": 0.7
            }
        )

        data = res.json()
        if "response" in data:
            reply = data["response"].strip()
        else:
            reply = f"❌ Error: {data.get('error', 'Unexpected response')}"
    except Exception as e:
        reply = f"❌ Exception: {e}"

    # Display assistant reply
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
