from flask import Flask, render_template, request, send_file
import os

from utils.pdf_reader import extract_text_from_pdf
from utils.docx_reader import extract_text_from_docx
from utils.matcher import calculate_match
from utils.section_checker import check_resume_sections
from utils.pdf_generator import generate_pdf

app = Flask(__name__)

analysis_result = {}

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

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
        analysis_result["strength"],
        analysis_result["matched"],
        analysis_result["missing"],
        analysis_result["feedback"],
    )

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
    