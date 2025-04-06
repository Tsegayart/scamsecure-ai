from fpdf import FPDF
import os

def generate_report(email, scam_type, message, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="ScamSecure AI - Forensic Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Scam Type: {scam_type}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Description: {message}")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Attached Evidence: {filename}", ln=True)

    os.makedirs('reports', exist_ok=True)
    report_filename = f"reports/{email.replace('@', '_at_')}_{filename}.pdf"
    pdf.output(report_filename)
    return report_filename
