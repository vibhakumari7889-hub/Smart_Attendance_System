# Smart Attendance System

A Python-based Smart Attendance System that uses Face Detection, Face Recognition, OpenCV, and SQLite to automate student attendance.

## Features

- Student registration with Student ID and Name
- Automatic face sample collection using webcam
- Face detection using OpenCV Haar Cascade
- Face recognition using LBPH algorithm
- Automatic attendance marking
- Prevents duplicate attendance on the same day
- View registered students
- View attendance records
- Export attendance report to CSV
- SQLite database for storing student and attendance data
- Modular project structure

## Technologies Used

- Python
- OpenCV
- OpenCV Contrib
- NumPy
- SQLite
- Pandas
- CSV

## Project Structure

Smart_Attendance_System/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── attendance.db
│
├── dataset/
│   └── students/
│
├── models/
│   ├── haarcascade_frontalface_default.xml
│   ├── face_model.yml
│   └── label_map.json
│
├── reports/
│   └── attendance_report.csv
│
└── src/
    ├── database.py
    ├── registration.py
    ├── recognition.py
    ├── attendance.py
    ├── reports.py
    └── __init__.py

## How It Works

1. Register a student using their Student ID and Name.
2. The webcam captures multiple face samples.
3. Face samples are stored locally for model training.
4. Train the LBPH face recognition model.
5. Start the attendance system.
6. The webcam detects and recognizes registered students.
7. Attendance is automatically recorded in the SQLite database.
8. A student can only be marked present once per day.
9. Attendance records can be viewed or exported as a CSV report.

## Installation

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## Run the Application

python main.py

## Main Menu

1. Register Student
2. Train Face Recognition Model
3. Start Attendance
4. View Attendance Report
5. Export Attendance to CSV
6. View Registered Students
7. Exit

## Database

SQLite is used to store:

- Student information
- Attendance records
- Date and time of attendance
- Attendance status

## Attendance Reports

Attendance records can be exported to:

reports/attendance_report.csv

## Important Note

Face datasets, trained models, databases, and generated reports contain locally generated data and are excluded from GitHub using .gitignore.

## Future Improvements

- Graphical User Interface (GUI)
- Admin login and authentication
- Monthly attendance statistics
- Attendance percentage calculation
- Email notifications
- Cloud database integration
- Web-based attendance dashboard

## Author

Vibha Kumari

B.Tech Information Technology Student

Smart Attendance System developed using Python, OpenCV, and SQLite.