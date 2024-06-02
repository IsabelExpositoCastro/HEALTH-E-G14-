import streamlit as st

# Function to simulate user login
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

def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")
