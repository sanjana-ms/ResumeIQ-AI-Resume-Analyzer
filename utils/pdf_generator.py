from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(filename, percentage, grade, strength,
                 matched, missing, feedback):

    c = canvas.Canvas(filename, pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 18)
    c.drawString(180, y, "Resume Analysis Report")

    y -= 40

    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"ATS Score : {percentage}%")
    y -= 20

    c.drawString(50, y, f"Grade : {grade}")
    y -= 20

    c.drawString(50, y, f"Strength : {strength}")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Matched Skills")
    y -= 20

    c.setFont("Helvetica", 12)

    for skill in matched:
        c.drawString(70, y, f"• {skill}")
        y -= 18

    y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Missing Skills")
    y -= 20

    c.setFont("Helvetica", 12)

    for skill in missing:
        c.drawString(70, y, f"• {skill}")
        y -= 18

    y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Feedback")
    y -= 20

    c.setFont("Helvetica", 12)
    c.drawString(50, y, feedback)

    c.save()