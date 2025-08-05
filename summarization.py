"""
Text Summarization Module

Overview:
-> Users can paste any text data into the Streamlit interface.
-> The input text will be processed and summarized using a pre-trained large language model (LLM).
-> The summarized output will be displayed directly within the Streamlit UI.

Inputs:
-> Raw text content provided by the user via the Streamlit app.

Outputs:
-> Concise summarized version of the input text.

Approach:
-> Streamlit UI collects user input.
-> A pre-trained LLM generates a summary.
-> The result is rendered in the Streamlit interface for easy viewing.
"""
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Set page configuration
st.markdown(
    """
    <style>
        .stApp {
            background-color:  #EEE1FF; /* Light purple background */
        }
        div[data-basewebui="input"] > div {
            background-color: white !important;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
        }
        input, textarea {
            background-color: white !important;
            color: black;
        }
        h1 {
            color: #4B0082; /* Indigo color for headings */
            text-align: center;
        }
        .caption-text {
            font-size: 16px;
            color: #333333;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Add Title
st.markdown("<h1> 📝 SnapSummary</h1>", unsafe_allow_html=True)
# Add caption
st.markdown('<p class="caption-text"><i>Turn long text into short insights—fast, clean, and easy.</i></p>', unsafe_allow_html=True)
# Add subtitle
st.markdown("<h4 style='color:indigo;'>✍️ Enter your text below to generate a summary</h4>", unsafe_allow_html=True)

# Text input area
user_input = st.text_area(" ", placeholder="Paste your content here...")

# Only run summarization if there's user input
if user_input:
    # Load environment variables
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    #print("Loaded API Key:", "API Key found" if API_KEY else "No API Key found")
    genai.configure(api_key=API_KEY)

    # Prompt setup
    system_message = "You are a helpful assistant that summarizes text."
    prompt = f"{system_message}\n\n{user_input}"

    # Gemini model
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    # Display summary
    st.write("#### ✨ Summary")
    st.write(response.text)

