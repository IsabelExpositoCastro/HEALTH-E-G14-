import streamlit as st
from modules.ChatBot import run_chatbot

def display():
    st.header("Consult ChatBot")
    run_chatbot()
