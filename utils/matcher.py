import re

# List of common technical skills
SKILLS = [
    "python", "java", "c", "c++", "javascript",
    "html", "css", "bootstrap", "tailwind",
    "react", "angular", "vue",
    "node.js", "express",
    "flask", "django",
    "spring", "spring boot", "hibernate",
    "sql", "mysql", "mongodb", "postgresql",
    "git", "github",
    "aws", "docker", "kubernetes",
    "linux", "rest api",
    "machine learning", "artificial intelligence",
    "data structures", "algorithms",
    "numpy", "pandas", "tensorflow", "pytorch",
    "power bi", "tableau", "excel"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = sorted(set(resume_skills) & set(job_skills))
    missing = sorted(set(job_skills) - set(resume_skills))

    if len(job_skills) == 0:
        percentage = 0
    else:
        percentage = round((len(matched) / len(job_skills)) * 100)

    if percentage >= 80:
        feedback = "Excellent! Your resume matches the job description very well."
        grade = "A"
        strength = "🟢 Excellent Resume"

    elif percentage >= 60:
        feedback = "Good! Your resume matches many required skills but can be improved."
        grade = "B"
        strength = "🔵 Good Resume"

    elif percentage >= 40:
        feedback = "Average. Consider adding more relevant skills."
        grade = "C"
        strength = "🟠 Average Resume"

    else:
        feedback = "Poor match. Your resume needs significant improvements."
        grade = "D"
        strength = "🔴 Needs Improvement"

    return matched, missing, percentage, feedback, grade, strength