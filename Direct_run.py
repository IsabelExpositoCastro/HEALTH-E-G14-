import subprocess

def main():
    # Activate the virtual environment
    activate_cmd = r"venv\Scripts\activate"
    subprocess.run(activate_cmd, shell=True)

    # Run the Streamlit app
    streamlit_cmd = f"streamlit run file_name.py"
    subprocess.run(streamlit_cmd, shell=True)

if __name__ == "__main__":
    main()