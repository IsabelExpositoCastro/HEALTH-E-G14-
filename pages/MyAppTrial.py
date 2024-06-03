# Import necessary libraries
import os
import streamlit as st
from openai import OpenAI
import json
from datetime import date, timedelta
from modules.logout import logout  # Correct import statement
from modules.login import login 
from modules.validate_signup import validate_signup
from modules.createAccount import createAccount
from modules.ChatBot import run_chatbot

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
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        background-color: #007bff;
        color: #fff;
    }
    .header img {
        cursor: pointer;
    }
    .header-options {
        display: flex;
        align-items: center;
    }
    .header-options button, .header-options a {
        margin-left: 15px;
        background-color: transparent;
        color: #fff;
        border: none;
        cursor: pointer;
        text-decoration: none;
    }
    .header-options button:hover, .header-options a:hover {
        text-decoration: underline;
    }
    .profile-dropdown {
        position: absolute;
        right: 10px;
        top: 50px;
        background-color: #fff;
        color: #000;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        display: none;
    }
    .profile-dropdown.show {
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize "database"
with open('database.json', 'r') as file:
    users = json.load(file)

# Initialize session state variable if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main function to run the app
def main():
    # Initialize session state variable if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "creating_account" not in st.session_state:
        st.session_state.creating_account = False
    if "selected_menu" not in st.session_state:
        st.session_state.selected_menu = "Home"

    # Header with navigation options
    st.markdown("""
        <div class='header'>
            <img src='image.png' width='50' onclick="window.location.reload()">
            <div class='header-options'>
                <button onclick="window.location.href='/'">Who are we?</button>
                <button onclick="window.location.href='/?page=chatbot'">Consult ChatBot</button>
                <button onclick="window.location.href='/?page=notifications'">🔔 Notifications</button>
                <button id="profile-btn">👤 Profile</button>
                <button onclick="window.location.href='/?page=login'">Login/Logout</button>
            </div>
        </div>
        <div id='profile-dropdown' class='profile-dropdown'>
            <p onclick="window.location.href='/?page=my_account'">My Account</p>
            <p onclick="window.location.href='/?page=privacy_security'">Privacy & Security</p>
            <p onclick="window.location.href='/?page=saved_prescriptions'">My Saved Prescriptions</p>
            <p onclick="window.location.href='/?page=appointments'">See My Appointments</p>
            <p onclick="window.location.href='/?page=contact_us'">Contact Us</p>
        </div>
        <script>
            document.getElementById('profile-btn').onclick = function() {
                document.getElementById('profile-dropdown').classList.toggle('show');
            }
        </script>
    """, unsafe_allow_html=True)

    # Handle navigation
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["home"])[0]

    # Login page
    if not st.session_state.logged_in:
        if st.session_state.creating_account:
            st.header("Create Account")
            if createAccount(users):
                st.session_state.creating_account = False
        else:
            st.header("Login")
            if login(users):
                st.session_state.logged_in = True
            if st.button("Sign Up"):
                st.session_state.creating_account = True
    
    # Navigation based on selected menu
    if st.session_state.logged_in:
        if page == "chatbot":
            st.subheader("Chatbot")
            run_chatbot()
        elif page == "notifications":
            st.subheader("Notifications")
            st.write("This is where you can view your notifications.")
            # Additional code for notifications goes here
        elif page == "my_account":
            st.subheader("My Account")
            container = st.container()
            with container:
                rows = []  # Store all rows in an array so they can be accessed later
                for field, value in st.session_state.user.items():
                    if field != "Password":
                        row = st.columns(2)
                        row[0].write(f"**{field}:**")
                        row[1].write(value)
                        rows.append(row)
        elif page == "privacy_security":
            st.subheader("Privacy & Security")
            st.write("This is where you can manage your privacy and security settings.")
            # Additional code for Privacy & Security goes here
        elif page == "saved_prescriptions":
            st.subheader("My Saved Prescriptions")
            st.write("This is where you can view your saved prescriptions.")
            # Additional code for My Saved Prescriptions goes here
        elif page == "appointments":
            st.subheader("Appointments")
            # Define appointment options
            appointment_options = ["Schedule New Appointment", "View Upcoming Appointments", "Appointment History"]
            appointment_icons = ["📅", "🕒", "📚"]
            
            # Display appointment options as buttons or icons
            option_columns = st.columns(len(appointment_options))
            for i, option in enumerate(appointment_options):
                if option_columns[i].button(f"{appointment_icons[i]} {option}"):
                    # Perform actions based on selected option
                    if option == "Schedule New Appointment":
                        st.write("This is where you can schedule a new appointment.")
                        # Additional code to schedule an appointment goes here
                    elif option == "View Upcoming Appointments":
                        st.write("This is where you can view your upcoming appointments.")
                        # Additional code to view upcoming appointments goes here
                    elif option == "Appointment History":
                        st.write("This is where you can view your appointment history.")
                        # Additional code to view appointment history goes here
        elif page == "contact_us":
            st.subheader("Contact Us")
            st.write("This is where you can contact us.")
            # Additional code for Contact Us goes here
        else:
            st.subheader("Home")
            st.write("Welcome to Health-E!")

# Run the app
if __name__ == "__main__":
    main()
