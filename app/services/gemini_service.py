import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def analyze_resume_with_ai(resume_text: str):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume below.

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT use markdown.
3. Do NOT use ```json.
4. Do NOT write any explanation before or after the JSON.

Return this exact structure:

{{
  "summary": "",
  "strengths": [],
  "weaknesses": [],
  "missing_skills": [],
  "recommended_roles": [],
  "career_roadmap": [],
  "resume_tips": []
}}

Resume:

{resume_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        print("\n========== RAW GEMINI RESPONSE ==========\n")
        print(text)
        print("\n=========================================\n")

        # Remove markdown if Gemini returns it
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        # Parse JSON
        return json.loads(text)

    except json.JSONDecodeError:
        return {
            "summary": text,
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "recommended_roles": [],
            "career_roadmap": [],
            "resume_tips": [
                "Gemini returned non-JSON output."
            ]
        }

    except Exception as e:
        print("\n========== GEMINI ERROR ==========")
        print(type(e).__name__)
        print(e)
        print("==================================\n")

        return {
            "summary": "AI analysis could not be completed.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "recommended_roles": [],
            "career_roadmap": [],
            "resume_tips": [str(e)]
        }