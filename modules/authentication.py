import streamlit as st

def login():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Dummy validation
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True
            return True
        else:
            st.error("Invalid email or password")
            return False

def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")
