import streamlit as st
from openai import OpenAI

def interact_with_chatbot(user_input, messages):
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Call OpenAI's chat completion API to interact with the chatbot
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages + [{"role": "user", "content": user_input}],
    )
    return chat_completion.choices[0].message.content

def display_chatbot():
    st.subheader("Chatbot")
    user_input = st.text_input("You: ")
    if st.button("Send"):
        if user_input:
            # Get previous chat messages
            messages = st.session_state.messages
            response = interact_with_chatbot(user_input, messages)
            st.write("Health-E Chatbot:", response)
            # Append user input and bot response to messages
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": response})
