import re

def check_resume_sections(text):

    text = text.lower()

    sections = {
        "Email": bool(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)),
        "Phone": bool(re.search(r"\d{10}", text)),
        "Education": "education" in text,
        "Experience": "experience" in text,
        "Projects": "project" in text,
        "Skills": "skills" in text,
        "Certifications": "certification" in text or "certifications" in text
    }

    return sections