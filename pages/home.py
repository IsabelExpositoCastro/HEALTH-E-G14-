import streamlit as st
import pandas as pd

def display(user):
    st.subheader("Menu")
    user_1 = st.session_state.user
    # Define account options
    account_options = ["My Account", "Privacy & Security", "My Saved Prescriptions", "See My Appointments", "Contact Us"]
    account_icons = ["👤", "🔒", "💊", "📅", "📞"]
    
    # Display account options as buttons or icons
    account_columns = st.columns(len(account_options))
    for i, option in enumerate(account_options):
        if account_columns[i].button(f"{account_icons[i]} {option}"):
            # Perform actions based on selected option
            if option == "My Account":
                st.subheader("My Account")
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
                st.write("At HEALTH-E, our goal is to provide you with the best possible experience. If you have any suggestions or comments on how we can improve, we'd love to hear from you. Thank you for trusting us with your healthcare needs.")
                # Additional code for Contact Us goes here
                
