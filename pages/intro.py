import streamlit as st
from pages import profile
from modules.login import login
from modules.createAccount import createAccount
from MyAppTrial import set_page
from pages import profile

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

        # set_page("home")
        # home.display()
        
