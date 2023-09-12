from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-resume')
def download_resume():
    resume_path = 'resume.pdf'
    return send_file(resume_path, as_attachment=True)

if __name__ == '__main__':
    # Start the Flask application with HTTP
    app.run(host="0.0.0.0", port=8080)
