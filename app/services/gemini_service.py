import os
import json

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume_with_ai(resume_text: str):
    prompt = f"""
You are an expert ATS recruiter and career coach.

Analyze the resume below.

Return ONLY valid JSON.

Use exactly this structure:

{{
  "summary":"",
  "ats_score":0,
  "strengths":[],
  "weaknesses":[],
  "missing_skills":[],
  "recommended_roles":[],
  "career_roadmap":[],
  "resume_tips":[]
}}

Resume:

{resume_text}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown if Gemini wraps JSON in ```json ... ```
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "error": "Gemini returned an invalid JSON response.",
            "raw_response": text
        }