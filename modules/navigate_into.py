import streamlit as st

def navigate_to(section):
    if section == "Home":
        # Add functionality to go to home page
        pass
    elif section == "Who are we?":
        # Add functionality to go to "Who are we?" section
        pass
    elif section == "Consult chatbot":
        # Add functionality to go to chatbot section
        pass
    elif section == "Log out":
        # Add functionality to log out
        pass
    elif section == "Profile":
        st.write("Profiiiiiiiiileeeeeeeeee")
        st.session_state.selected_menu = "Account Options"