from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import traceback

from app.services.resume_parser import extract_text_from_pdf
from app.services.resume_analyzer import analyze_resume
from app.services.ats_score import calculate_ats
from app.services.gemini_service import analyze_resume_with_ai

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.filename.lower().endswith((".pdf", ".docx")):
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed."
            )

        # Save uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text
        if file.filename.lower().endswith(".pdf"):
            extracted_text = extract_text_from_pdf(file_path)

        elif file.filename.lower().endswith(".docx"):
            raise HTTPException(
                status_code=501,
                detail="DOCX parsing is not implemented yet."
            )

        print("========== RESUME TEXT EXTRACTED ==========")

        # Resume Analysis
        resume_data = analyze_resume(extracted_text)

        print("========== RESUME ANALYZED ==========")

        # ATS Score
        ats_report = calculate_ats(resume_data)

        print("========== ATS SCORE GENERATED ==========")

        # AI Feedback
        print("========== CALLING GEMINI ==========")

        ai_feedback = analyze_resume_with_ai(extracted_text)

        print("========== GEMINI COMPLETED ==========")

        return {
            "message": "Resume uploaded successfully",
            "filename": file.filename,
            "resume": resume_data,
            "ats_report": ats_report,
            "ai_feedback": ai_feedback
        }

    except Exception:
        print("\n========== FULL ERROR TRACEBACK ==========\n")
        traceback.print_exc()
        print("\n==========================================\n")

        raise

    

       