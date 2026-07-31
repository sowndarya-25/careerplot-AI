import re


SKILLS = [
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


def analyze_resume(text: str):

    email = ""

    phone = ""

    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    if email_match:
        email = email_match.group()

    phone_match = re.search(
        r'(\+91[- ]?)?\d{10}',
        text
    )

    if phone_match:
        phone = phone_match.group()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    name = lines[0] if lines else ""

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": found_skills
    }