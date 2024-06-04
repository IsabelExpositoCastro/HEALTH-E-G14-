import streamlit as st
telephone_number = "(34) 123 123 123"
def display():
    st.header("How to contact us?")
    st.write("Email :   support@healthe.com")
    st.write("Phone number:    ")
    st.markdown(f'<a href="tel:+1234567890">{telephone_number}</a>', unsafe_allow_html=True)