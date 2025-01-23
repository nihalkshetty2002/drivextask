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

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")
if api_key is None:
    st.error("API key not found. Please set the environment variable 'API_KEY'")
    st.stop()

client = Groq(api_key=api_key)

def get_model_response(user_input):
    try:
        # Handle greetings
        greetings = ["hello", "hi", "hey", "goodbye", "bye"]
        if any(greet in user_input.lower() for greet in greetings):
            if "bye" in user_input.lower() or "goodbye" in user_input.lower():
                return "Goodbye! Have a nice day!"
            return "Hello! How can I assist you with the excel document today?"

        # Prepare prompt
        prompt = f"Excel content:\n{st.session_state.excel_content}\n\nUser question: {user_input}" if st.session_state.excel_content else user_input
        
        # Get response from Groq
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0.2,
            max_tokens=4096
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar for file upload
with st.sidebar:
    st.header("📁 Upload Excel File")
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
    
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.session_state.excel_content = df.to_string()
            st.success("✅ File uploaded successfully!")
            st.dataframe(df, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

# Main chat interface
st.title("💬 AI Document Assistant")
st.markdown("---")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Get and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_model_response(prompt)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and Groq AI*")

# Run with specific port
if __name__ == "__main__":
    os.environ['STREAMLIT_SERVER_PORT'] = '8501'
    os.environ['STREAMLIT_SERVER_ADDRESS'] = 'localhost'