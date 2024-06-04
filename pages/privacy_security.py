import streamlit as st
from pages import contact_us

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
        <div class="title">PRIVACY & SECURITY</div>
        <div class="content">
            <p>We take the privacy and security of your data very seriously. HEALTH-E is designed to protect your personal and medical information, ensuring that your data is always secure and private. Our mission is to make healthcare accessible and convenient, without compromising the confidentiality and security of your data.</p>
            <p>With HEALTH-E, you can rest assured that all your interactions and data are protected using advanced encryption techniques. We implement top-level security measures, such as strong authentication and continuous monitoring, to safeguard your information against unauthorized access.</p>
            <p>In addition, we comply with the strictest privacy regulations, ensuring that your information is handled with the utmost care and in accordance with legal standards. We are committed to providing you with the tools and information you need to manage your health effectively, with the peace of mind that your data is protected.</p>
            <p>Join us at HEALTH-E and experience accessible and secure healthcare, from the comfort of your mobile device. Your privacy and security are our priority.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    if st.button("📞 Contact Us"):
        contact_us.display()