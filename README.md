# Features of AI Document Assistant
The AI Document Assistant is a Streamlit-based application designed to simplify interactions with Excel documents using AI. Below are the key features of the application:

1. User-Friendly Interface
The app provides a clean and interactive UI built with Streamlit.
Users can interact with the AI directly via a chat interface.


2. Excel File Upload
Users can upload Excel files (.xlsx or .xls) directly through the sidebar.
The app reads the uploaded file and converts its content into a readable format for AI interaction.
The uploaded file's content is displayed as a scrollable, styled DataFrame for easy review.


3. AI-Powered Chat Assistance
Powered by the Groq API, the app can answer user queries about the uploaded Excel file.
Example use cases:
Summarize data in the Excel file.
Provide insights or statistical analysis based on the content.
Answer specific questions, such as finding values, trends, or anomalies.
Handle general inquiries or greet users with a friendly tone.


4. Session State Management
Session persistence ensures that the chat history and uploaded Excel file content are maintained during the session.
Users can have an uninterrupted conversation with the AI while referring to previously uploaded files.


5. Dynamic Prompt Construction
If an Excel file is uploaded, the AI combines the file's content with the user's query to provide contextually relevant responses.
If no file is uploaded, the AI defaults to handling general queries.


6. Natural Language Understanding
Supports natural conversation:
Recognizes greetings and goodbyes, responding appropriately.
Handles specific document-related queries intelligently.


7. Interactive Chat System
Chat history is displayed in a threaded format:
User messages appear on the left.
AI responses appear on the right.
Provides real-time responses with a "Thinking..." spinner to improve user experience.


8. Error Handling
Displays user-friendly error messages when:
An invalid or unsupported file is uploaded.
The AI model encounters an error during query processing.


9. Configurable Settings
API key management: The application uses a .env file for securely storing the Groq API key.
Model configuration: The app uses the mixtral-8x7b-32768 model, optimized for document analysis and natural language conversations.


10. Cross-Platform Accessibility
Hosted locally using Streamlit, which allows users to interact with the app in their browser on localhost:8501.
Fully responsive layout that adapts to different screen sizes.

# Instruction for running the application locally
1. Download the Zip file

2. Under .env file use "PASTE YOUR API KEY"

3.Under Windowns bash run this command 
# pip install -r requirements.txt

4.Now run the application by using thi command
# streamlit run app.py


# Additional Details
Model Limitations:
When using the mixtral-8x7b-32768 model, it is important to note that there are constraints on the number of tokens that can be processed per request. If a request exceeds the token limit, the following error message will be displayed:

sql Copy Edit Request too large for model mixtral-8x7b-32768 in organization org_01jhfq9hs8f80v1wpng94pcexh service tier on_demand on tokens per minute (TPM): Limit 5000, Requested 63733, please reduce your message size and try again.

Cause: This error occurs when the token count in a request exceeds the allowed threshold of 5000 tokens per minute.
Solution: To avoid this error, reduce the size of your input or split the content into smaller chunks before sending the request.
