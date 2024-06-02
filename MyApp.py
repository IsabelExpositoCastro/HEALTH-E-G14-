# Import necessary libraries
import os
import streamlit as st
from openai import OpenAI
import json
from datetime import date, timedelta

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

# Function to validate the signup form
def validate_signup(name, dateOfBirth, gender, bloodType, phone, address, email, password):
    missing_fields = []
    if not name:
        missing_fields.append("Name")
    if not dateOfBirth:
        missing_fields.append("Date of Birth")
    if not gender:
        missing_fields.append("Gender")
    if not bloodType:
        missing_fields.append("Blood Type")
    if not phone:
        missing_fields.append("Phone Number")
    if not address:
        missing_fields.append("Address")
    if not email:
        missing_fields.append("Email")
    if not password:
        missing_fields.append("Password")
    
    return missing_fields

def createAccount():
    name = st.text_input("Name")
    dateOfBirth = st.date_input("Date of Birth", format="DD/MM/YYYY", min_value=date.today() - timedelta(days=365*125),
                                max_value=date.today(), value=None)
    gender = st.selectbox("Gender", ("Male", "Female", "Non-Binary", "Other"))
    bloodType = st.selectbox("Blood Type", ("A+", "A-", "B+", "AB+", "O+", "O-"))
    familyDoctor = st.text_input("Family Doctor")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")
    email = st.text_input("New Email")
    password = st.text_input("New Password", type="password")
    
    if st.button("Register"):
        missing_fields = validate_signup(name, dateOfBirth, gender, bloodType, phone, address, email, password)
        if not missing_fields:
            if email not in users:
                users[email] = {"Password": password,
                                "Name": name,
                                "Date of Birth": dateOfBirth.strftime("%d-%m-%Y"),
                                "Gender": gender,
                                "Blood Type": bloodType,
                                "Family Doctor": familyDoctor,
                                "Email": email,
                                "Phone": phone,
                                "Address": address}
                with open("database.json", 'w') as newFile:
                    json.dump(users, newFile, indent=4)
                st.success("Account created successfully!")
                return True
            else:
                st.error("Email already exists. Please use a different email.")
        else:
            st.error(f"The following fields are missing or incomplete: {', '.join(missing_fields)}")
    else:
        return False

# Function to log out the user
def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")

# Main function to run the app
def main():
    # Initialize session state variable if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "creating_account" not in st.session_state:
        st.session_state.creating_account = False

    # Display image and centered title only in the first login/sign-in section
    if not st.session_state.logged_in:
        # Display an image as the title with a specified width
        st.image("image.png", width=200, use_column_width=True)  # Set the width as per your requirement

        # Centered title with separated parts
        st.markdown("<h1 style='text-align: center; color: #333;'>WHERE HEALTH MEETS AI<br>WHERE HEALTH MEETS EASE.</h1>", unsafe_allow_html=True)

    # Login page
    if not st.session_state.logged_in:
        
        if st.session_state.creating_account:
            st.header("Create Account")
            if createAccount():
                st.session_state.creating_account = False
        else:
            st.header("Login")
            if login():
                st.session_state.logged_in = True
            if st.button("Sign Up"):
                st.session_state.creating_account = True
        
    # After login
    else:
        # Top section with welcome text and logo
        top_section = st.columns([3, 1])
        top_section[0].header("Welcome to Health-E")
        if top_section[1].button("🏠"):
            st.session_state.selected_menu = "Account Options"
        
        # Add logout button
        if st.button("Logout"):
            logout()
        
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
