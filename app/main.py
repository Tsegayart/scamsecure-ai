from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from pdf_generator import generate_report

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    from flask import send_from_directory

    email = request.form.get('email')
    scam_type = request.form.get('scam_type')
    message = request.form.get('message')
    file = request.files.get('evidence')

    filename = None
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
    else:
        return "Invalid file type.", 400

    report_path = generate_report(email, scam_type, message, filename)

    return f"""
<div style='font-family: Arial; padding: 20px;'>
  <h2>✅ Scan Complete</h2>
  <p><strong>Scam Type:</strong> {scam_type}</p>
  <p><strong>Message:</strong> {message}</p>
  <p><strong>Evidence Uploaded:</strong> {filename}</p>
  <br>
  <a href='/{report_path}' target='_blank'>📄 Download Full PDF Report</a>
</div>
"""

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
