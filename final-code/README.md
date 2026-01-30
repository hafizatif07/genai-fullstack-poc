# AI Career Advice Generator

A web application that generates personalized career advice using Google's Generative AI (Gemini).

## What It Does

1. **Collects user information** through an HTML form (name, email, education, career goals)
2. **Sends data to Flask backend** running on Python
3. **Calls Google's Gemini API** to generate personalized career advice
4. **Displays results** with token usage information

---

## Quick Start

### Prerequisites
- Python 3.8+
- Google API Key (free from https://aistudio.google.com/app/apikey)
- VS Code or any text editor

### Setup (5 minutes)

1. **Get API Key**
   - Visit https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key

2. **Configure .env**
   - Edit `.env` file
   - Paste: `GOOGLE_API_KEY=your_key_here`

3. **Install Dependencies**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run Flask Backend** (Terminal 1)
   ```powershell
   python app.py
   ```

5. **Run HTML Server** (Terminal 2)
   ```powershell
   python -m http.server 3000
   ```

6. **Open Browser**
   - Visit http://localhost:3000
   - Fill form and click "Generate Career Advice"

---

## Project Files

### Core Files
- **`app_simple.py`** - Main Flask backend (clean, minimal comments)
- **`config.py`** - Loads Google API credentials
- **`index.html`** - Frontend form and UI
- **`.env`** - API key (never commit this!)
- **`requirements.txt`** - Python dependencies

### Key Features
- ✅ Google Generative AI (Gemini) integration
- ✅ Token usage tracking
- ✅ Error handling with helpful messages
- ✅ Clean, documented code

---
