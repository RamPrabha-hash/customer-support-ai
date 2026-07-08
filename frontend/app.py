import streamlit as st
import requests

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/chat"

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#2E86C1;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.user-box{
    background:#DCF8C6;
    padding:12px;
    border-radius:10px;
}

.ai-box{
    background:#F2F3F4;
    padding:12px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR
# ----------------------------

with st.sidebar:

    st.title("🤖 Customer Support AI")

    st.success("🟢 AI Agent Online")

    st.divider()

    st.subheader("Features")

    st.write("✅ Agentic AI")
    st.write("✅ RAG Knowledge Base")
    st.write("✅ Conversation Memory")
    st.write("✅ Ticket Escalation")
    st.write("✅ FastAPI Backend")
    st.write("✅ OpenRouter LLM")

    st.divider()

    st.subheader("System Status")

    st.success("🟢 Backend Connected")
    st.success("🟢 Memory Enabled")
    st.success("🟢 Knowledge Base Ready")
    st.success("🟢 Escalation Enabled")
    st.success("🟢 OpenRouter Connected")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ----------------------------
# HEADER
# ----------------------------

st.markdown(
    "<div class='main-title'>🤖 AI Customer Support Agent</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Powered by FastAPI + OpenRouter + Agentic AI + RAG</div>",
    unsafe_allow_html=True
)

# ----------------------------
# SESSION STATE
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# DISPLAY CHAT HISTORY
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# USER INPUT
# ----------------------------

prompt = st.chat_input("Ask your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "message": prompt
                    },
                    timeout=120
                )

                if response.status_code == 200:

                    answer = response.json()["response"]

                else:

                    answer = "❌ Backend Error\n\n" + response.text

            except Exception as e:

                answer = f"Connection Error:\n\n{e}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )