import streamlit as st
def display_header():
        st.markdown(
            """
            <div class="header">
                <div>
                    <img src="image.png" alt="App Logo" style="width: 50px; cursor: pointer;" onclick="location.href='.'">
                </div>
                <div class="header-btns">
                    <button onclick="document.getElementById('notifications').click()">🔔 Notifications</button>
                    <button onclick="document.getElementById('who_are_we').click()">Who are we?</button>
                    <button onclick="document.getElementById('consult_chatbot').click()">Consult ChatBot</button>
                    <button onclick="document.getElementById('log_out').click()">Log Out</button>
                    <button onclick="document.getElementById('profile').click()">👤 Profile</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )