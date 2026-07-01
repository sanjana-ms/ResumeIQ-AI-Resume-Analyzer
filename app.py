from flask import Flask, render_template, request, send_file, redirect, url_for, session, flash
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

from utils.pdf_reader import extract_text_from_pdf
from utils.docx_reader import extract_text_from_docx
from utils.matcher import calculate_match
from utils.section_checker import check_resume_sections
from utils.pdf_generator import generate_pdf

app = Flask(__name__)
app.secret_key= "resumeiq_secret_key"

analysis_result = {}

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check passwords
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("register"))

        # Hash password
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect("resumeiq.db")
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO users(name, email, password)
                VALUES (?, ?, ?)
            """, (name, email, hashed_password))

            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()
            flash("Email already exists . Please login", "danger")
            return redirect(url_for("register"))
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("resumeiq.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, password FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):

            session["user_id"] = user[0]
            session["user_name"] = user[1]

            return redirect(url_for("home"))

        flash("Invalid email or password!" , "danger")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():

   session.clear()

   flash("Logged out successfully!", "success")

   return redirect(url_for("home"))

@app.route("/upload", methods=["POST"])
def upload():
    if "user_id" not in session:
        flash("Account created successfully! Please login", "success")
        return redirect(url_for(login))
    global analysis_result

    resume = request.files["resume"]
    job_description = request.form["job_description"]

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    resume.save(file_path)

    extension = os.path.splitext(resume.filename)[1].lower()

    if extension == ".pdf":
       resume_text = extract_text_from_pdf(file_path)

    elif extension == ".docx":
       resume_text = extract_text_from_docx(file_path)

    else:
       return "Unsupported file format. Please upload a PDF or DOCX file."
    sections = check_resume_sections(resume_text)

    matched, missing, percentage, feedback, grade, strength = calculate_match(
        resume_text,
        job_description
    )

    # Store latest analysis for PDF download
    analysis_result = {
        "percentage": percentage,
        "grade": grade,
        "strength": strength,
        "matched": matched,
        "missing": missing,
        "feedback": feedback,
        "job_description" : job_description,
    }

    return render_template(
        "result.html",
        percentage=percentage,
        matched=matched,
        missing=missing,
        feedback=feedback,
        grade=grade,
        strength=strength,
        sections=sections,
    )


@app.route("/download")
def download():

    filename = "Resume_Report.pdf"

    generate_pdf(
        filename,
        analysis_result["percentage"],
        analysis_result["grade"],
    
        analysis_result["matched"],
        analysis_result["missing"],
        analysis_result["feedback"],
        analysis_result["job_description"],
    )

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
