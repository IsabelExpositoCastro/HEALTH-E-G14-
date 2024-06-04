import streamlit as st

def display():
    # Set the page configuration
    # Custom CSS to style the app
    st.markdown("""
        <style>
        .main {
            text-align: center;
            padding-top: 100px;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #2E86C1;
        }
        .content {
            font-size: 1.5em;
            color: #566573;
        }
        </style>
        """, unsafe_allow_html=True)

    # Centered container with the content
    st.markdown("""
    <div class="main">
        <div class="title">WHO ARE WE?</div>
        <div class="content">
            <p>Welcome to HEALTH-E, the innovative healthcare accessibility application designed to transform your healthcare experience. Our mission is to make healthcare more accessible and convenient by allowing you to wait at home instead of in hospital or center queues.</p>
            <p>With HEALTH-E, you can speak with our medically trained chatbot for seamless appointment scheduling and accurate symptom assessments. We aim to empower you with the tools and information you need to manage your health effectively, all from the comfort of your mobile device.</p>
            <p>Join us in revolutionizing healthcare accessibility with a user-friendly mobile app that makes it easier for everyone to get the care they need.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
