# HEALTH-E (G14)
This repository will be used to work on our Software project: HEALTH-E

# Health-E App

Health-E is a web application that provides users with functionalities such as a chatbot, appointments, and profile management. This application is built using Streamlit and OpenAI's GPT-3.5-turbo model.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.7+
- Streamlit
- OpenAI Python API library
- dotenv (optional, for managing environment variables)

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies.

```bash
git clone <your-repository-url>
cd your-repository-name
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

# Configuration
Create a .env file in the root directory of your project and add your OpenAI API key.
[In bash terminal]
```bash
export OPENAI_API_KEY="your_openai_api_key"
```
Or manualy from Environment Variables configuration.

# Running the Application
To run the application, use the Streamlit CLI:
```bash
streamlit run MyApp.py
```
# Usage
- Login:
Enter your email and password on the login page.
Use the dummy credentials: user@example.com and password.

- Chatbot:
After logging in, navigate to the Chatbot page from the sidebar.
Enter your message in the input field and click 'Send'.
The chatbot will respond to your message.

- Appointments:
Navigate to the Appointments page from the sidebar.
This section is reserved for future functionality.

- Profile:
Navigate to the Profile page from the sidebar.
This section is reserved for future functionality.

- Logout:
Click the 'Logout' button to log out of the application.
