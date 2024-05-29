import streamlit as st
from modules import chatbot, appointments, authentication, health_info

def main():
    st.title("Health-E App")

    # Authentication
    user_authenticated = authentication.login()

    if user_authenticated:
        st.header("Welcome to Health-E")

        # Add logout button
        if st.button("Logout"):
            authentication.logout()

        # Menu options
        menu = st.sidebar.selectbox("Menu", ["Chatbot", "Appointments", "Profile"])

        # Display selected menu option
        if menu == "Chatbot":
            chatbot.display_chatbot()
        elif menu == "Appointments":
            appointments.display_appointments()
        elif menu == "Profile":
            st.subheader("Profile")
            st.write("This is where the profile management functionality will go.")

if __name__ == "__main__":
    main()
