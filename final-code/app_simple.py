"""
Simple Flask app for beginners

Purpose:
- Receive form data (JSON) from `index.html`
- Build a short prompt and send it to Google Generative AI (Gemini)
- Return the AI text back to the webpage

Usage:
1. Create and activate a Python venv
   python -m venv venv
   venv\Scripts\activate
2. Install dependencies:
   pip install -r requirements.txt
3. Add `GOOGLE_API_KEY` to your `.env` file
4. Run:
   python app_simple.py

This file is intentionally minimal for teaching newcomers.
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError("Missing GOOGLE_API_KEY in .env. See README_FIRST.txt for setup.")

# Configure the Google Generative AI client
genai.configure(api_key=API_KEY)

# Create Flask app
app = Flask(__name__)
CORS(app)  # allow requests from the browser


@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    """Receive JSON form data, call Google AI, return text.

    Expected JSON structure (from the form):
    {
      "name": "Alice",
      "email": "alice@example.com",
      "situation": "student",
      "studies": ["GCSEs in Maths and English"],
      "goal": "Software developer"
    }
    """
    data = request.get_json() or {}

    # Simple, readable extraction with safe defaults
    name = data.get('name', 'Student')
    situation = data.get('situation', 'Not specified')
    studies = data.get('studies', [])
    goal = data.get('goal', 'Not specified')

    # Build a short prompt for the model
    studies_text = ', '.join(studies) if isinstance(studies, list) else str(studies)
    prompt = (
        f"Provide short, friendly career advice for the person below:\n"
        f"Name: {name}\n"
        f"Situation: {situation}\n"
        f"Education: {studies_text}\n"
        f"Career goal: {goal}\n\n"
        "Give 3 clear next steps the person can take."
    )

    # Call Google Generative AI (very simple call)
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)

    # The library returns text on `response.text`
    ai_text = getattr(response, 'text', str(response))

    return jsonify({'success': True, 'response': ai_text}), 200


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'model': MODEL}), 200


if __name__ == '__main__':
    print('Starting simple Flask app on http://127.0.0.1:5000')
    app.run(debug=True, port=5000)
