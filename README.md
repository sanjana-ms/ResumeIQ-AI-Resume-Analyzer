# AI Resume Analyzer & Job Application Tracker

## 📖 Project Overview

The **AI Resume Analyzer & Job Application Tracker** is a web application built using **Python** and **Flask**.

The goal of this project is to help users:

* Upload their resume (PDF)
* Analyze resume content
* Compare it with a job description
* Generate an ATS (Applicant Tracking System) score
* Identify missing skills
* Track job applications in one place

This project is being developed step by step as part of a hands-on learning journey with Flask and Python.

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML
* CSSYeah
* Bootstrap
* SQLite

---

## 🚧 Project Status


**Current Progress:** Learning Flask Basics ✅
## 📂 Project Structure

```text
ResumeAnalyzer/
│
├── app.py                  # Main Flask application
├── database.py             # Database connection and operations
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignored files
├── resumejob.db            # SQLite database
├── Resume_Report.pdf       # Generated resume analysis report
│
├── templates/              # HTML templates
│
├── static/                 # CSSYeah, JavaScript and images
│
├── uploads/                # Uploaded resume PDFs
│
└── utils/                  # Helper functions and resume analysis utilities
```
## ✨ Features

### 👤 User Authentication

* Secure user registration and login system.
* Session-based authentication for personalized access.

### 📄 Resume Upload

* Upload resumes in PDF format.
* Secure file handling and storage.

### 💼 Job Description Upload

* Upload or paste a job description for analysis.

### 🤖 AI Resume Analysis

* Extracts text from resumes.
* Identifies technical and soft skills.
* Compares resume content with the job description.

### 📊 ATS Score Calculation

* Calculates an ATS (Applicant Tracking System) compatibility score.
* Displays the score with a visual indicator.

### 🎯 Skill Gap Analysis

* Highlights missing skills required for the selected job.
* Suggests skills to improve resume effectiveness.

### 💡 Resume Improvement Suggestions

* Provides recommendations to strengthen the resume.
* Helps optimize resumes for ATS screening.

### 📑 PDF Report Generation

* Generates a downloadable Resume Analysis Report in PDF format.

### 📈 Dashboard

* Displays resume analysis results in a clean and interactive interface.

### 💾 Database Integration

* Stores user information and resume details using SQLite.

### 🎨 Responsive User Interface

* Built using HTML, CSS, Bootstrap, and Flask templates for a clean and user-friendly experience.

## 📸 Application Screenshots

### 🏠 Home Page

<img src="screenshots/home.png" width="100%">

The landing page introduces ResumeIQ and highlights its key capabilities, including ATS score prediction, skill matching, and AI-powered resume recommendations.

---

### 🚀 Features Section

<img src="screenshots/features.png" width="100%">

The Features section showcases the core functionalities of the application, including ATS Score Calculation, Smart Skill Matching, and AI-based Resume Recommendations.

---

### 📊 ATS Dashboard

<img src="screenshots/dashboard.png" width="100%">

The dashboard displays the calculated ATS score, matched skills, and missing skills, providing users with a quick overview of their resume performance.

---

### 📄 Resume Analysis Result

<img src="screenshots/result.png" width="100%">

The Resume Analysis page presents the final ATS score, identifies matched and missing skills, and provides actionable insights to improve resume quality.

## ⚙️ Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/sanjana-ms/ResumeIQ-AI-Resume-Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd ResumeIQ-AI-Resume-Analyzer
```

### 3. Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```
## ▶️ Running the Application

Start the Flask development server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The application will now be ready to use.

## 👩‍💻 Author

**M. Sushma Sanjana**

* 🎓 B.Tech in Computer Science and Engineering (AI & ML)
* 💻 Aspiring Software Engineer
* 🐍 Python | Java | Flask | HTML | CSS | SQL

### GitHub

https://github.com/sanjana-ms
⭐ If you found this project helpful, consider giving it a star on GitHub!
