import streamlit as st
import modal
import json
import os

# Streamlit configurations for blue theme
st.set_page_config(
    page_title="Podcast Newsletter",
    layout="wide",
    initial_sidebar_state="expanded",
    theme={
        "base": "dark",
        "primaryColor": "#0278AE",
        "backgroundColor": "#001F3F",
        "secondaryBackgroundColor": "#003366",
        "textColor": "#D9E6F2",
        "font": "sans serif"
    }
)

def main():
    st.title("Newsletter Dashboard")

    available_podcast_info = create_dict_from_json_files('.')

    # Left section - Input fields
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())

    if selected_podcast:
        # (The rest of the code remains unchanged...)

def create_dict_from_json_files(folder_path):
    # (The code for this function remains unchanged...)

def process_podcast_info(url):
    # (The code for this function remains unchanged...)

if __name__ == '__main__':
    main()
