from flask import Flask, request, render_template
import os
import sqlite3
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 * 1024 # 100GB

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS files
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     filename TEXT,
                     filepath TEXT,
                     uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.close()

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    rel_path = request.form.get('relPath', file.filename)

    # Normalize and secure
    rel_path = rel_path.replace("\\", "/")
    rel_path = os.path.normpath(rel_path)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], rel_path)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    file.save(save_path)

    # Insert into DB
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO files (filename, filepath) VALUES (?, ?)", (rel_path, save_path))
    conn.commit()
    conn.close()

    return '', 200

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
