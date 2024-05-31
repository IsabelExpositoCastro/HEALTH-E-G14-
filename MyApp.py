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

def createAccount():
    name = st.text_input("Name")
    dateOfBirth = st.date_input("Date of Birth", format="DD/MM/YYYY", min_value = date.today() - timedelta(days=365*125),
        max_value = date.today(), value = None)
    gender = st.selectbox("Gender", ("Male", "Female", "Non-Binary", "Other"))
    bloodType = st.selectbox("Blood Type", ("A+", "A-", "B+", "AB+", "AB-", "O+", "O-"))
    familyDoctor = st.text_input("Family Doctor")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")
    email = st.text_input("New Email")
    password = st.text_input("New Password", type = "password")
    if st.button("Register"):
        if email not in users and all([name, dateOfBirth, phone, email, password]):
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
                json.dump(users, newFile, indent = 4)
            return True
        else:
            st.error("All fields except \"Family Doctor\" are mandatory. Please fill them to continue.")
    else:
        return False
    
# Function to log out the user
def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")

# Main function to run the app
def main():
    # Display an image as the title
    #st.image("image.png", use_column_width=True)
    #st.markdown("<h1 style='text-align: center; color: #333;'>WHERE HEALTH MEETS AI<br>WHERE HEALTH MEETS EASE.</h1>", unsafe_allow_html=True)

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
        st.header("Welcome to Health-E")

        # Add logout button
        if st.button("Logout"):
            logout()
        
        # Menu options
        menu_items = ["Chatbot", "Appointments", "Profile"]
        menu_icons = ["💬", "📅", "👤"]
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

        # Profile page
        elif st.session_state.selected_menu == "Profile":
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
