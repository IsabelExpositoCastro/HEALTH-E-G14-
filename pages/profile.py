import streamlit as st
from pages import privacy_security

def display(user):
    st.subheader("Menu")
    user_1 = st.session_state.user
    # Define account options
    account_options = ["My Account", "Privacy & Security", "My Saved Prescriptions", "See My Appointments", "Contact Us"]
    account_icons = ["👤", "🔒", "💊", "📅", "📞"]
    
    # Display account options as buttons or icons
    account_columns = st.columns(len(account_options))
    for i, option in enumerate(account_options):
        if account_columns[i].button(f"{account_icons[i]} {option}", key=f"button_{i}"):
            # Perform actions based on selected option
            if option == "My Account":
                st.write("This is where you can view and edit your account information.")
                container = st.container()
                with container:
                    rows = [] # Store all rows in an array so they can be accessed later
                    #print(st.session_state.user)
                    for field, value in user_1.items():
                        
                        if field != "Password":
                            row = st.columns(2)
                            row[0].write(f"**{field}:**")
                            row[1].write(value)
                            rows.append(row)
            elif option == "Privacy & Security":
                privacy_security.display()
                # Additional code for Privacy & Security goes here
            elif option == "My Saved Prescriptions":
                st.write("This is where you can view your saved prescriptions.")
                # Additional code for My Saved Prescriptions goes here
            elif option == "See My Appointments":
                st.write("This is where you can view your appointments.")
                # Additional code for See My Appointments goes here
            elif option == "Contact Us":
                st.write("This is where you can contact us.")
                # Additional code for Contact Us goes here