import streamlit as st
import json
from modules.logout import logout
from modules.login import login
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
        padding: 20px;
        background-color: #007bff;
        color: #fff;
    }
    .header img {
        width: 50px;
        cursor: pointer;
    }
    .header-btns {
        display: flex;
        align-items: center;
    }
    .header-btns button {
        margin-left: 10px;
        background-color: transparent;
        color: #fff;
        border: none;
        cursor: pointer;
    }
    .header-btns button:hover {
        text-decoration: underline;
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
    # Initialize session state variables if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "creating_account" not in st.session_state:
        st.session_state.creating_account = False
    if "selected_menu" not in st.session_state:
        st.session_state.selected_menu = "Chatbot"

    # Define the header section with interactive buttons
    def display_header():
        
        
        notifications_clicked = st.button("🔔 Notifications", key='notifications')
        who_are_we_clicked = st.button("Who are we?", key='who_are_we')
        consult_chatbot_clicked = st.button("Consult ChatBot", key='consult_chatbot')
        log_out_clicked = st.button("Log Out", key='log_out')
        profile_clicked = st.button("👤 Profile", key='profile')

        # Handle button actions
        if notifications_clicked:
            st.write("Notifications clicked")
        if who_are_we_clicked:
            st.write("Who are we? clicked")
        if consult_chatbot_clicked:
            st.session_state.selected_menu = "Chatbot"
        if log_out_clicked:
            st.session_state.logged_in = False
            st.experimental_rerun()
        if profile_clicked:
            st.session_state.selected_menu = "Account Options"

    # Handle button clicks
    

    # Display image and centered title only in the first login/sign-in section
    if not st.session_state.logged_in:
        # Display an image as the title with a specified width
        st.image("image.png", width=200, use_column_width=True)
        # Centered title with separated parts
        st.markdown("<h1 style='text-align: center; color: #333;'>WHERE HEALTH MEETS AI<br>WHERE HEALTH MEETS EASE.</h1>", unsafe_allow_html=True)

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
        
    # After login
    else:
        # Display the header
        display_header()
        
        st.header("Welcome to Health-E")
        
        
        # Menu options
        menu_items = ["Chatbot", "Appointments"]
        menu_icons = ["💬", "📅"]
        menu_columns = st.columns(len(menu_items))

        # Define selected menu
        if "selected_menu" not in st.session_state:
            st.session_state.selected_menu = menu_items[0]

        # Display menu items with icons
        for i, item in enumerate(menu_items):
            if menu_columns[i].button(f"{menu_icons[i]} {item}"):
                st.session_state.selected_menu = item

        # Chatbot page
        if st.session_state.selected_menu == "Chatbot":
            st.subheader("Chatbot")
            run_chatbot()

        # Appointments page
        elif st.session_state.selected_menu == "Appointments":
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

        # Account Options section
        if st.session_state.selected_menu == "Account Options":
            st.subheader("Account Options")

            # Define account options
            account_options = ["My Account", "Privacy & Security", "My Saved Prescriptions", "See My Appointments", "Contact Us"]
            account_icons = ["👤", "🔒", "💊", "📅", "📞"]
            
            # Display account options as buttons or icons
            account_columns = st.columns(len(account_options))
            for i, option in enumerate(account_options):
                if account_columns[i].button(f"{account_icons[i]} {option}"):
                    # Perform actions based on selected option
                    if option == "My Account":
                        st.write("This is where you can view and edit your account information.")
                        container = st.container()
                        with container:
                            rows = [] # Store all rows in an array so they can be accessed later
                            for field, value in st.session_state.user.items():
                                if field != "Password":
                                    row = st.columns(2)
                                    row[0].write(f"**{field}:**")
                                    row[1].write(value)
                                    rows.append(row)
                    elif option == "Privacy & Security":
                        st.write("This is where you can manage your privacy and security settings.")
                        # Additional code for Privacy & Security goes here
                    elif option == "My Saved Prescriptions":
                        st.write("This is where you can view your saved prescriptions.")
                        # Additional code for My Saved Prescriptions goes here
                    elif option == "See My Appointments":
                        st.write("This is where you can view your appointments.")
                        # Additional code for See My Appointments goes here
                    elif option == "Contact Us":
                        st.write("This is where you can contact us.")
                        # Additional code for Contact Us goes here

# Run the app
if __name__ == "__main__":
    main()
