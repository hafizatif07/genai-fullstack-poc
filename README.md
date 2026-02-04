# genai-fullstack-poc
This repo will consist of the a full working solution to embed the LLM with the front end and act as a chat bot 
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

### Setup (5 minutes) — (Requires Python 3.12.4)

**Note:** This project is tested with **Python 3.12.4**. If your machine has a newer Python (e.g., 3.14.x) you do not need to replace system Python — install Python 3.12.4 and create a venv that uses that interpreter (instructions below).

1. **Get API Key**
   - Visit https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key (see guidance below if your account has age restrictions)

2. **Configure .env**
   - In the `final-code` folder create/edit `.env`
   - Add: GOOGLE_API_KEY="your_key_here" 

3. **Install Python 3.12.4 & create a venv (Mac & Windows)**

   macOS (official installer)
   - Official installer: download Python 3.12.4 from https://www.python.org/downloads/macos/

   - Create venv and activate:
     ```bash
     python3.12 -m venv .venv
     source .venv/bin/activate
     python -m pip install --upgrade pip setuptools wheel
     python -m pip install -r requirements.txt
     ```

   Windows (installer or py launcher)
   - Download Python 3.12.4 from https://www.python.org/downloads/windows/
   - Or use py launcher if installed:
     ```powershell
     py -3.12 -m venv .venv
     .\.venv\Scripts\Activate.ps1    # PowerShell
     # or .\.venv\Scripts\activate  # cmd.exe
     python -m pip install --upgrade pip setuptools wheel
     python -m pip install -r requirements.txt
     ```

   Downgrade note: If you already have a higher Python installed, **install 3.12.4 separately** (installer/conda/pyenv) and make a fresh venv with that interpreter. Do not modify or remove your system Python.

4. **Run the Flask backend (final-code directory)**
   - Default: `python app_simple.py` (binds to 127.0.0.1:5000 by default)
   - If port 5000 is occupied (e.g., macOS AirPlay uses 5000), run on another port:
     ``
     # edit app_simple.py to change app.run(port=5001)
     ```

5. **Run the static HTML server (final-code directory)**
   ```bash
   python -m http.server 3000
   ```
   - Open http://localhost:3000 in your browser and use the form.

6. **Verify installation & CORS (curl checks)**
   - Health check (GET):
     ```bash
     curl -i http://127.0.0.1:5000/health
     ```
   - CORS preflight (OPTIONS):
     ```bash
     curl -i -X OPTIONS http://127.0.0.1:5000/generate-prompt \
       -H "Origin: http://localhost:3000" \
       -H "Access-Control-Request-Method: POST" \
       -H "Access-Control-Request-Headers: Content-Type"
     ```
     You should see `Access-Control-Allow-Origin` in the response headers if CORS is configured.

   - POST test (simulate browser request):
     ```bash
     curl -i -X POST http://127.0.0.1:5000/generate-prompt \
       -H "Origin: http://localhost:3000" \
       -H "Content-Type: application/json" \
       -d '{"name":"Test","email":"t@example.com","situation":"student","studies":["GCSEs"],"goal":"career advice"}'
     ```

7. **Google API Key guidance & age restrictions**
   - Keep API keys secret: store in `.env` and **do not commit** the key to source control.
   - Google may place restrictions on account access for certain users (including age or regional requirements). If your account is underage or restricted, you may not be able to create or use an API key without parental/guardian consent or an organization-managed account. Review Google AI Studio / Cloud account sign-up policies if unsure.
   - Consider creating a restricted API key in the Google console and monitor usage/quotas.


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
