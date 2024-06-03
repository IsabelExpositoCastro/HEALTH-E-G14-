import streamlit as st
import pandas as pd
import json
from modules.logout import logout
from modules.login import login 
from modules.createAccount import createAccount
from pages import notifications, who_we_are, consult_chatbot, profile, intro, home

st.markdown("""
            <style>
                body {
                    font-family: 'Helvetica Neue', sans-serif;
                    background-color: #f0f2f6;
                }
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

# Function to set the current page
def set_page(page_name):
    st.session_state.current_page = page_name
    
# Function to log out the user
def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out successfully.")

# Main function to run the app
def main():
    
    # Initialize session state variables if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "creating_account" not in st.session_state:
        st.session_state.creating_account = False
    if "current_page" not in st.session_state:
        st.session_state.current_page = "intro"
    if "user" not in st.session_state:
        st.session_state.user = None

    # Reset session state when navigating to a new page
    if "previous_page" in st.session_state and st.session_state.previous_page != st.session_state.current_page:
        for key in st.session_state.keys():
            if key not in ["logged_in", "creating_account", "current_page"]:
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
    if st.session_state.current_page == "home":
        #home.display()
        st.subheader("Menu")

        # Define account options
        account_options = ["Privacy & Security", "My Saved Prescriptions", "See My Appointments", "Contact Us"]
        account_icons = ["🔒", "💊", "📅", "📞"]
        
        # Display account options as buttons or icons
        account_columns = st.columns(len(account_options))
        for i, option in enumerate(account_options):
            if account_columns[i].button(f"{account_icons[i]} {option}"):
                # Perform actions based on selected option
                if option == "Privacy & Security":
                    st.subheader("Privacy & Security")
                    st.write("We take the privacy and security of your data very seriously. HEALTH-E is designed to protect your personal and medical information, ensuring that your data is always secure and private. Our mission is to make healthcare accessible and convenient, without compromising the confidentiality and security of your data.")
                    st.write("With HEALTH-E, you can rest assured that all your interactions and data are protected using advanced encryption techniques. We implement top-level security measures, such as strong authentication and continuous monitoring, to safeguard your information against unauthorized access.")
                    st.write("In addition, we comply with the strictest privacy regulations, ensuring that your information is handled with the utmost care and in accordance with legal standards. We are committed to providing you with the tools and information you need to manage your health effectively, with the peace of mind that your data is protected.")
                    st.write("Join us at HEALTH-E and experience accessible and secure healthcare, from the comfort of your mobile device. Your privacy and security are our priority.")
                    # Additional code for Privacy & Security goes here
                elif option == "My Saved Prescriptions":
                    st.subheader("My Saved Prescriptions")

                    # Example prescription data
                    prescription_data = {
                        "PRESCRIPTION": ["Paracetamol 1g", "Frenadol Forte (sobres)", "Ibuprofeno 600mg"],
                        "STARTING DATE": ["22/05/2022", "12/03/2023", "12/03/2023"],
                        "ENDING DATE": ["25/05/2022", "17/03/2023", "17/03/2023"]
                    }
                    
                    df = pd.DataFrame(prescription_data)
                    st.table(df)
                    # Additional code for My Saved Prescriptions goes here
                elif option == "See My Appointments":
                    st.subheader("My Appointments")
                    
                    cols = st.columns([1, 2, 1])
                    with cols[1]:
                        if st.button("Future Appointments"):
                            st.write("Displaying future appointments...")

                        if st.button("Past Appointments"):
                            st.write("Displaying past appointments...")
                        # Additional code for See My Appointments goes here
                elif option == "Contact Us":
                    st.subheader("Contact Us")
                    st.write("We would love to hear from you! At HEALTH-E, we are here to help you and answer all your questions.")
                    st.write("If you have any queries, comments or need assistance with our application, please do not hesitate to contact us via the options below:")
                    lst = [' E-mail: info@healthe.com', 'Phone: +0034 900 100 200']
                    for i in lst:
                        st.markdown("- " + i)
                    st.write("Customer service hours: Monday to Friday, 9:00 AM - 6:00 PM (Local Time)")
                    st.write("At HEALTH-E, our goal is to provide you with the best possible experience.\
                            If you have any suggestions or comments on how we can improve, we'd love to hear from you. \
                            Thank you for trusting us with your healthcare needs.")

                    # Additional code for Contact Us goes here
    if st.session_state.current_page == "notifications":
        notifications.display()
    if st.session_state.current_page == "who_we_are":
        who_we_are.display()
    if st.session_state.current_page == "consult_chatbot":
        consult_chatbot.display()
    if st.session_state.current_page == "profile":
        #profile.display()
        st.subheader("My Profile")
        container = st.container()
        with container:
            rows = [] # Store all rows in an array so they can be accessed later
            #print(st.session_state.user)
            for field, value in st.session_state.user.items():
                if field != "Password":
                    row = st.columns(2)
                    row[0].write(f"**{field}:**")
                    row[1].write(value)
                    rows.append(row)

# Run the app
if __name__ == "__main__":
    main()
