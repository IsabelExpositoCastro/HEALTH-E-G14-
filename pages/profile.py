import streamlit as st
import pandas as pd
from pages import privacy_security, contact_us

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
                contact_us.display()
                # Additional code for Contact Us goes here