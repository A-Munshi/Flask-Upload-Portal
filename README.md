## 📂 Flask Upload Portal
A modern **Flask web application** for uploading **multiple files and folders** with real-time progress tracking, attractive animations, and database logging.  
This project demonstrates how to combine **Flask (backend)**, **SQLite (database)**, and a **responsive frontend (HTML, CSS, JS)** to build a seamless file upload portal.  

### Repo Structure
```
flask-file-uploader/
│
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
![Upload UI](screenshots/upload-ui.png)

#### Real-time Progress  
![Upload Progress](screenshots/upload-progress.png)

#### Upload Success  
![Upload Success](screenshots/upload-success.png)

#### Database Logging  
![Database Records](screenshots/db-view.png)

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
git clone https://github.com/<your-username>/flask-advanced-uploader.git
cd flask-advanced-uploader
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
🔗 [LinkedIn](www.linkedin.com/in/anuvab-munshi) • [GitHub](github.com/A-Munshi)

```
