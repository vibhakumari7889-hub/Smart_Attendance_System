# Smart Attendance System

## 🚀 Live Demo

[Open Smart Attendance System](https://smartattendancesystem-cmgcb5fmihqyku3jv4pynv.streamlit.app/)

The application is deployed using Streamlit Community Cloud and can be accessed directly from a web browser.

A Python-based Smart Attendance System that automates student attendance using **OpenCV, Face Detection, LBPH Face Recognition, and SQLite**.

## Features

- Student registration with Student ID and Name
- Automatic face sample collection using webcam
- Face detection using Haar Cascade
- Face recognition using LBPH algorithm
- Automatic attendance marking
- Prevents duplicate attendance on the same day
- View registered students
- View attendance records
- Export attendance reports to CSV
- SQLite database for student and attendance management
- Modular Python project structure
- 🌐 Live Streamlit web application
- 📱 Browser-based camera capture for web deployment

## Technologies Used

- Python
- OpenCV
- OpenCV Contrib
- NumPy
- SQLite
- CSV
- Streamlit

## Project Structure

```text
Smart_Attendance_System/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│
├── dataset/
│   └── students/
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
└── src/
    ├── database.py
    ├── registration.py
    ├── recognition.py
    ├── attendance.py
    ├── reports.py
    └── __init__.py
```
Note: Face datasets, SQLite database files, trained models, and generated reports are stored locally and excluded from GitHub using .gitignore.

Skip to content
vibhakumari7889-hub
Smart_Attendance_System
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
vibhakumari7889-hub
Smart_Attendance_System
Public
Go to file
t
T
vibhakumari7889-hub
vibhakumari7889-hub
Fix README formatting
8bd6757
 · 
3 minutes ago
Name		
models
Initial commit: Smart Attendance System
17 hours ago
src
Clean up project dependencies
15 hours ago
.gitignore
Initial commit: Smart Attendance System
17 hours ago
README.md
Fix README formatting
3 minutes ago
app.py
Add Streamlit web app
12 hours ago
main.py
Initial commit: Smart Attendance System
17 hours ago
requirements.txt
Fix OpenCV dependency for Streamlit Cloud
11 hours ago
Repository files navigation
README
Smart Attendance System
🚀 Live Demo
Open Smart Attendance System

The application is deployed using Streamlit Community Cloud and can be accessed directly from a web browser.

A Python-based Smart Attendance System that automates student attendance using OpenCV, Face Detection, LBPH Face Recognition, and SQLite.

Features
Student registration with Student ID and Name
Automatic face sample collection using webcam
Face detection using Haar Cascade
Face recognition using LBPH algorithm
Automatic attendance marking
Prevents duplicate attendance on the same day
View registered students
View attendance records
Export attendance reports to CSV
SQLite database for student and attendance management
Modular Python project structure
🌐 Live Streamlit web application
📱 Browser-based camera capture for web deployment
Technologies Used
Python
OpenCV
OpenCV Contrib
NumPy
SQLite
CSV
Streamlit
Project Structure
Smart_Attendance_System/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│
├── dataset/
│   └── students/
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
└── src/
    ├── database.py
    ├── registration.py
    ├── recognition.py
    ├── attendance.py
    ├── reports.py
    └── __init__.py
Note: Face datasets, SQLite database files, trained models, and generated reports are stored locally and excluded from GitHub using .gitignore.

Skip to content
vibhakumari7889-hub
Smart_Attendance_System
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
vibhakumari7889-hub
Smart_Attendance_System
Public
Go to file
t
T
vibhakumari7889-hub
vibhakumari7889-hub
Fix README formatting
8bd6757
 · 
3 minutes ago
Name		
models
Initial commit: Smart Attendance System
17 hours ago
src
Clean up project dependencies
15 hours ago
.gitignore
Initial commit: Smart Attendance System
17 hours ago
README.md
Fix README formatting
3 minutes ago
app.py
Add Streamlit web app
12 hours ago
main.py
Initial commit: Smart Attendance System
17 hours ago
requirements.txt
Fix OpenCV dependency for Streamlit Cloud
11 hours ago
Repository files navigation
README
Smart Attendance System
🚀 Live Demo
Open Smart Attendance System

The application is deployed using Streamlit Community Cloud and can be accessed directly from a web browser.

A Python-based Smart Attendance System that automates student attendance using OpenCV, Face Detection, LBPH Face Recognition, and SQLite.

Features
Student registration with Student ID and Name
Automatic face sample collection using webcam
Face detection using Haar Cascade
Face recognition using LBPH algorithm
Automatic attendance marking
Prevents duplicate attendance on the same day
View registered students
View attendance records
Export attendance reports to CSV
SQLite database for student and attendance management
Modular Python project structure
🌐 Live Streamlit web application
📱 Browser-based camera capture for web deployment
Technologies Used
Python
OpenCV
OpenCV Contrib
NumPy
SQLite
CSV
Streamlit
Project Structure
Smart_Attendance_System/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│
├── dataset/
│   └── students/
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
└── src/
    ├── database.py
    ├── registration.py
    ├── recognition.py
    ├── attendance.py
    ├── reports.py
    └── __init__.py
Note: Face datasets, SQLite database files, trained models, and generated reports are stored locally and excluded from GitHub using .gitignore.

How It Works Register a student using their Student ID and Name. The webcam captures face samples. Face samples are stored locally for model training. Train the LBPH face recognition model. Start the attendance system. The system detects and recognizes registered students. Attendance is automatically recorded in SQLite. Duplicate attendance for the same student on the same day is prevented. Attendance records can be viewed or exported as a CSV report. Installation

Clone the Repository git clone https://github.com/vibhakumari7889-hub/Smart_Attendance_System.git cd Smart_Attendance_System
Create a Virtual Environment python -m venv .venv
Activate the Virtual Environment
On Windows PowerShell:

.venv\Scripts\Activate.ps1 4. Install Dependencies pip install -r requirements.txt Run the Application Streamlit Web App streamlit run app.py Command-Line Application python main.py Main Menu

Register Student
Train Face Recognition Model
Start Attendance
View Attendance Report
Export Attendance to CSV
View Registered Students
Exit Database
The system uses SQLite to store:

Student information Attendance records Attendance date and time Attendance status Attendance Reports

Attendance records can be exported as:

reports/attendance_report.csv Privacy Note

Face images and generated biometric-related data are stored locally. These files are intentionally excluded from the public GitHub repository using .gitignore.

Future Improvements Graphical User Interface (GUI) Admin authentication Attendance percentage calculation Monthly attendance statistics Email notifications Cloud database integration Web-based attendance dashboard Author

Vibha Kumari

B.Tech Information Technology Student

Built using Python, OpenCV, SQLite, and Streamlit.

About

Python-based Smart Attendance System using OpenCV, LBPH Face Recognition, and SQLite for automated attendance management.

Topics
Resources
Readme
Activity
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
1
 (1)
@vibhakumari7889-hub
vibhakumari7889-hub
Languages
Python
100%
Suggested workflows
Based on your tech stack

Pylint logo
Pylint
Lint a Python application with pylint.
By GitHub Actions
Publish Python Package logo
Publish Python Package
Publish a Python Package to PyPI on release.
By GitHub Actions
Python application logo
Python application
Create and test a Python application.
By GitHub Actions
More workflows
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
 
