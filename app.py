import streamlit as st
import pandas as pd
from groq import Groq
import os
from dotenv import load_dotenv

# Configure page
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'excel_content' not in st.session_state:
    st.session_state.excel_content = None
