from fpdf import FPDF
import os

def generate_report(email, scam_type, message, filename):
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "ScamSecure AI - Scan Report", ln=True, align="C")
            self.ln(10)

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Scam Type: {scam_type}", ln=True)
    pdf.multi_cell(0, 10, f"Message:\n{message}")
    pdf.cell(0, 10, f"Evidence File: {filename}", ln=True)

    # Basic "fake AI" mock analysis
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Preliminary Analysis:", ln=True)
    pdf.set_font("Arial", "", 12)
    if "investment" in message.lower():
        pdf.multi_cell(0, 10, "- ⚠️ Potential fake investment scheme detected.")
    elif "wallet" in message.lower() or "crypto" in message.lower():
        pdf.multi_cell(0, 10, "- ⚠️ Possible crypto wallet phishing attempt.")
    else:
        pdf.multi_cell(0, 10, "- No strong scam indicators found in this brief scan.")

    # Save PDF
    report_folder = "reports"
    os.makedirs(report_folder, exist_ok=True)
    report_name = f"{filename}.pdf"
    report_path = os.path.join(report_folder, report_name)
    pdf.output(report_path)

    return os.path.join(report_folder, report_name)
