import streamlit as st
from pages import home
from modules.login import login
from modules.createAccount import createAccount
from MyAppTrial import set_page

def display(users):
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
            
    else:
        st.markdown("<h2 style='text-align: center;'>Welcome to Health-E</h2>", unsafe_allow_html=True)


def login(users):
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
        

def createAccount(users):
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