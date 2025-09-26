## 📂 Flask Upload Portal
A modern **Flask web application** for uploading **multiple files and folders** with real-time progress tracking, attractive animations, and database logging.  
This project demonstrates how to combine **Flask (backend)**, **SQLite (database)**, and a **responsive frontend (HTML, CSS, JS)** to build a seamless file upload portal.  

### Repo Structure
```
Flask-Upload-Portal/│
├── app.py                  # Main Flask app
├── database.db             # Example SQLite DB (with some sample entries)
├── uploads/                # Sample uploaded files
│   ├── sample1.txt
│   └── demo-folder/
│
├── templates/
│   └── index.html          # Frontend UI
│
├── requirements.txt        # Flask, sqlite3, etc.
```
### Demo Preview
#### Upload Interface  
<img width="2880" height="1698" alt="UploadUI" src="https://github.com/user-attachments/assets/cfa94241-f92a-455d-9234-52dacdae2d1b" />

#### Real-time Progress  
<img width="2880" height="1698" alt="UploadProgress" src="https://github.com/user-attachments/assets/309502b5-5081-49a1-a554-19f74d38fd38" />

#### Upload Success  
<img width="2880" height="1696" alt="UploadSuccess" src="https://github.com/user-attachments/assets/36ba3c68-8a67-4188-9069-4110a560e567" />

#### Database Logging  
<img width="1039" height="473" alt="DatabaseLogging" src="https://github.com/user-attachments/assets/d1aa0324-5788-4d33-adf2-df381044bdce" />

### Features
- 📁 **Multi-file & multi-folder uploads**  
- 📊 **Real-time upload progress bar with animations**  
- 🗄️ **SQLite database integration** to store upload details  
- 🎨 **Responsive and modern UI** (HTML, CSS, JavaScript)  
- 💾 Supports uploads up to **5 GB**  
- 🛠️ Well-structured code with Flask best practices  

### Tech Stack
- **Backend:** Python (Flask)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Storage:** Local filesystem (`/uploads/` directory)  

### How It Works
1. User selects one or more files/folders.  
2. Uploads are tracked in real-time with a progress bar.  
3. Files are stored inside the `uploads/` directory.  
4. Upload details are automatically recorded in the SQLite database (`database.db`).  

### Installation & Setup
Clone the repository:
```
git clone https://github.com/A-Munshi/Flask-Upload-Portal.git
cd Flask-Upload-Portal
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the Flask app:
```
python app.py
```

Open in browser:
```
http://127.0.0.1:5000/
```

### Future Improvements
* 🔒 Add user authentication for secure uploads
* ☁️ Integrate with cloud storage (Azure Blob, AWS S3, or Google Cloud)
* 📤 Enable file sharing via unique download links
* 🧾 Admin panel for managing uploads


### Author
Developed by **Anuvab Munshi**
