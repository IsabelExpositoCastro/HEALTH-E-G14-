import os
import streamlit as st
from openai import OpenAI
import json

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize "database"
with open('database.json', 'r') as file:
    users = json.load(file)

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
        # Check if email and password are correct
        if email in users and users[email]['Password'] == password:
            st.session_state.logged_in = True  # Initialize session state variable
            st.session_state.user = users[email]
            return True
        else:
            st.error("Invalid email or password")
            return False
        
#def createAccount():
    #email = st.text_input("Email")
    #password = st.text_input("Password")

# Function to log out the user
def logout():
    st.session_state.logged_in = False
    del st.session_state.user
    st.success("You have been logged out successfully.")

# Main function to run the app
def main():
    st.title("Health-EFTESTING App")

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
            appointments_submenu = st.selectbox("Select Option", ["Schedule New Appointment", "View Upcoming Appointments", "Appointment History"])

            if appointments_submenu == "Schedule New Appointment":
                st.write("This is where you can schedule a new appointment.")
                # Additional code to schedule an appointment goes here

            elif appointments_submenu == "View Upcoming Appointments":
                st.write("This is where you can view your upcoming appointments.")
                # Additional code to view upcoming appointments goes here

            elif appointments_submenu == "Appointment History":
                st.write("This is where you can view your appointment history.")
                # Additional code to view appointment history goes here

        # Profile page
        elif menu == "Profile":
            st.subheader("Profile")
            container = st.container()
            with container:
                rows = [] # Store all rows in an array so they can be accessed later
                for field, value in st.session_state.user.items():
                    if field != "Password":
                        row = st.columns(2)
                        row[0].write(f"**{field}:**")
                        row[1].write(value)
                        rows.append(row)

# Run the app
if __name__ == "__main__":
    main()
