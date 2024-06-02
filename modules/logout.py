import streamlit as st

# Function to log out the user
def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")