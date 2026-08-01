"""
ATS Score Calculator for CareerPilot AI
"""

AI_ML_SKILLS = [
    "Python",
    "Java",
    "C",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Reinforcement Learning",
    "FastAPI",
    "Git",
    "Power BI",
    "Tableau",
    "DBMS",
    "OOP",
    "DSA"
]


def calculate_ats(resume_data):
    """
    Calculates an ATS score based on detected skills.
    """

    skills = resume_data.get("skills", [])

    matched_skills = []
    missing_skills = []

    for skill in AI_ML_SKILLS:
        if skill in skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_skills = len(AI_ML_SKILLS)
    matched_count = len(matched_skills)

    ats_score = round((matched_count / total_skills) * 100)

    strengths = []

    if "Python" in matched_skills:
        strengths.append("Strong Python Programming")

    if "Java" in matched_skills:
        strengths.append("Good Java Programming")

    if "Machine Learning" in matched_skills:
        strengths.append("Machine Learning Knowledge")

    if "Deep Learning" in matched_skills:
        strengths.append("Deep Learning Experience")

    if "NLP" in matched_skills:
        strengths.append("Natural Language Processing Skills")

    if "SQL" in matched_skills:
        strengths.append("Database Knowledge")

    if "Git" in matched_skills:
        strengths.append("Version Control Experience")

    if "Power BI" in matched_skills:
        strengths.append("Data Visualization Skills")

    # Overall Level
    if ats_score >= 90:
        level = "Excellent"
    elif ats_score >= 75:
        level = "Very Good"
    elif ats_score >= 60:
        level = "Good"
    elif ats_score >= 40:
        level = "Average"
    else:
        level = "Needs Improvement"

    # Recommended Roles
    recommended_roles = []

    if "Machine Learning" in matched_skills:
        recommended_roles.append("Machine Learning Engineer")

    if "Deep Learning" in matched_skills:
        recommended_roles.append("AI Engineer")

    if "NLP" in matched_skills:
        recommended_roles.append("NLP Engineer")

    if "SQL" in matched_skills:
        recommended_roles.append("Data Analyst")

    if "Power BI" in matched_skills:
        recommended_roles.append("Business Intelligence Analyst")

    if not recommended_roles:
        recommended_roles.append("Software Developer")

    return {
        "ats_score": ats_score,
        "level": level,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "recommended_roles": recommended_roles
    }