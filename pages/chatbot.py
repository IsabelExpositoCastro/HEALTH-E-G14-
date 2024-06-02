import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import time

# App title
st.set_page_config(page_title="💬 HealthBot")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f6;
    }
    .chat-message {
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 80%;
    }
    .chat-message.user {
        background-color: #d1e7dd;
        color: #0f5132;
        align-self: flex-end;
    }
    .chat-message.assistant {
        background-color: #f8d7da;
        color: #842029;
        align-self: flex-start;
    }
    .stButton button {
        background-color: #007bff;
        color: #fff;
    }
    .stButton button:hover {
        background-color: #0056b3;
        color: #fff;
    }
    .stTextInput input {
        background-color: #e9ecef;
        color: #495057;
    }
    .stTextInput input:focus {
        background-color: #fff;
        color: #495057;
    }
    </style>
    """, unsafe_allow_html=True)

# Hugging Face Credentials
with st.sidebar:
    st.title('💬 HealthBot')
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
        hf_email = st.secrets['EMAIL']
        hf_pass = st.secrets['PASS']
    else:
        hf_email = st.text_input('Enter E-mail:', type='password')
        hf_pass = st.text_input('Enter password:', type='password')
        if not (hf_email and hf_pass):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')

# Store LLM generated responses
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"<div class='chat-message {message['role']}'>{message['content']}</div>", unsafe_allow_html=True)

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    string_dialogue = "You are a helpful healthcare assistant. Users seek your assistance to address their health-related concerns and questions about illnesses they may be experiencing. Depending on the severity of the situation or upon request, you provide help in scheduling an appointment with a doctor."

    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"

    prompt = f"{string_dialogue} {prompt_input} Assistant: "
    return chatbot.chat(prompt).text  # Ensure the response is a string

# User-provided prompt
prompt = st.chat_input(disabled=not (hf_email and hf_pass))
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div class='chat-message user'>{prompt}</div>", unsafe_allow_html=True)

# Generate a new response if last message is not from assistant
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_placeholder = st.empty()
            full_response = generate_response(prompt, hf_email, hf_pass)

            response = ""
            for chunk in full_response.split():
                response += chunk + " "
                response_placeholder.markdown(f"<div class='chat-message assistant'>{response}</div>", unsafe_allow_html=True)
                time.sleep(0.1)  # Adjust the delay for a better typing effect

    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
