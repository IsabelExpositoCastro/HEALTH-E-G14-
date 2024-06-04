import streamlit as st
telephone_number = "(34) 123 123 123"
def display():
    st.header("How to contact us?")
    st.write("We would love to hear from you! At HEALTH-E, we are here to help you and answer all your questions.")
    st.write("If you have any queries, comments or need assistance with our application, please do not hesitate to contact us via the options below:")
    lst = [' E-mail: info@healthe.com', 'Phone: +0034 900 100 200']
    for i in lst:
        st.markdown("- " + i)
    st.write("Customer service hours: Monday to Friday, 9:00 AM - 6:00 PM (Local Time)")
    st.write("At HEALTH-E, our goal is to provide you with the best possible experience. If you have any suggestions or comments on how we can improve, we'd love to hear from you. Thank you for trusting us with your healthcare needs.")
    