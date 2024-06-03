import streamlit as st
import json
from modules.logout import logout
from modules.login import login
from modules.createAccount import createAccount
from pages import notifications, who_we_are, consult_chatbot, profile, intro, home

st.markdown("""
    <style>
        .stButton button {
            background-color: #2D4AF7;
            color: #fff;
        }
        .stButton button:hover {
            background-color: #1031F9;
            color: #fff;
        }
    </style>
    """, unsafe_allow_html=True)

# Initialize "database"
with open('database.json', 'r') as file:
    users = json.load(file)

# Initialize session state variables if not already initialized
if "user" not in st.session_state:
    st.session_state.user = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "creating_account" not in st.session_state:
    st.session_state.creating_account = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "intro"

def set_page(page_name):
    st.session_state.current_page = page_name

def main():
    # Reset session state when navigating to a new page
    if "previous_page" in st.session_state and st.session_state.previous_page != st.session_state.current_page:
        for key in list(st.session_state.keys()):
            if key not in ["logged_in", "creating_account", "current_page", "user"]:
                del st.session_state[key]

    st.session_state.previous_page = st.session_state.current_page

    if st.session_state.logged_in:
        # Display header buttons
        with st.container():
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            if col1.button("🔔 Notifications", key="notifications_btn"):
                set_page("notifications")
            if col2.button("Who are we?", key="who_we_are_btn"):
                set_page("who_we_are")
            if col3.button("Consult ChatBot", key="consult_chatbot_btn"):
                set_page("consult_chatbot")
            if col4.button("Log In/Out", key="logout_btn"):
                st.session_state.logged_in = False
                st.session_state.user = {}
                set_page("intro")
                logout()
            if col5.button("🏠", key="home_btn"):
                set_page("home")
            if col6.button("👤 Profile", key="profile_btn"):
                set_page("profile")

    if not st.session_state.logged_in:
        # Display an image as the title with a specified width
        st.image("image.png", width=200, use_column_width=True)  # Set the width as per your requirement

        # Centered title with separated parts
        st.markdown("<h1 style='text-align: center; color: #333;'>WHERE HEALTH MEETS AI<br>WHERE HEALTH MEETS EASE.</h1>", unsafe_allow_html=True)

    # Page content based on the current page
    if st.session_state.current_page == "intro":
        intro.display(users)
    elif st.session_state.current_page == "home":
        home.display(user)
    elif st.session_state.current_page == "notifications":
        notifications.display()
    elif st.session_state.current_page == "who_we_are":
        who_we_are.display()
    elif st.session_state.current_page == "consult_chatbot":
        consult_chatbot.display()
    elif st.session_state.current_page == "profile":
        profile.display()

if __name__ == "__main__":
    main()
