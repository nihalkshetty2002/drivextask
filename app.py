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

