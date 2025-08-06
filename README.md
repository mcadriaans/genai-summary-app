# 📝 SnapSummary

Turn long text into short insights—fast, clean, and easy.

## 📦 Overview

SnapSummary is a Streamlit-powered web app that allows users to paste in raw text and instantly receive a concise summary using a large language model (LLM). It's designed to be lightweight, beautiful, and lightning-fast.

## 🎯 Features

- 🔹 Paste any amount of text into the interface
- 🔹 Automatically generates a clean summary using Google's Gemini LLM
- 🔹 Displays results within an elegant Streamlit UI

## 📁 Project Structure
```
📁 genai-summary-app/ 
|--> 🐍 summarization.py # Main application script 
|--> 🔐 .env # Contains API key for Gemini (not committed) 
|--> 📋 requirements.txt # Python dependencies └── README.md # You're here!
```

## 🔑 Environment Variables

This app uses an API key to access Gemini. Create a `.env` file in the root directory and add:
```python
GOOGLE_API_KEY=your-google-api-key-here
```

Make sure `.env` is placed alongside `summarization.py`.

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/genai-summary-app.git
   cd genai-summary-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Add your .env file with the Google API key (see above)**.

## Run the App
```bash
streamlit run summarization.py
```
By default, the app will launch at http://localhost:8501.
If deploying on a cloud server like AWS EC2, make sure port 8501 is open in your security group and replace localhost with your instance’s public IP.


## 🌟 App Preview

Here’s what SnapSummary looks like in action:

![SnapSummary Screenshot](/screenshot.png)

## 💬 Credits
Made with 💜 using Streamlit + Gemini by Michéle.


