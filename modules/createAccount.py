import json
import streamlit as st
from datetime import date, timedelta
from modules import validate_signup

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
