import os
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize session state variable if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to interact with the AI chatbot
def interact_with_chatbot(user_input, messages):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the GPT-3 model to use
        messages=messages + [{"role": "user", "content": user_input}],  # Concatenate previous messages with new user input
    )
    return chat_completion.choices[0].message.content

# Function to simulate user login
def login():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check if email and password are correct (dummy validation)
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True  # Initialize session state variable
            return True
        else:
            st.error("Invalid email or password")
            return False

# Function to log out the user
def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")

# Main function to run the app
def main():
    st.title("Health-E App")

    # Initialize session state variable if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Login page
    if not st.session_state.logged_in:
        st.header("Login")
        if login():
            st.session_state.logged_in = True

    # After login
    else:
        st.header("Welcome to Health-E")

        # Add logout button
        if st.button("Logout"):
            logout()

        # Menu options
        menu = st.sidebar.selectbox("Menu", ["Chatbot", "Appointments", "Profile"])

        # Chatbot page
        if menu == "Chatbot":
            st.subheader("Chatbot")
            user_input = st.text_input("You: ")
            if st.button("Send"):
                if user_input:
                    # Get previous chat messages
                    messages = [m["content"] for m in st.session_state.messages if m["role"] != "assistant"]
                    response = interact_with_chatbot(user_input, messages)
                    st.write("Health-E Chatbot:", response)
                    # Append user input and bot response to messages
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.messages.append({"role": "assistant", "content": response})

        # Appointments page
        elif menu == "Appointments":
            st.subheader("Appointments")
            st.write("This is where the appointments functionality will go.")

        # Profile page
        elif menu == "Profile":
            st.subheader("Profile")
            st.write("This is where the profile management functionality will go.")

# Run the app
if __name__ == "__main__":
    main()