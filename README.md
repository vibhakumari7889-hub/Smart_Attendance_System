# Smart Attendance System

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

## Technologies Used

- Python
- OpenCV
- OpenCV Contrib
- NumPy
- SQLite
- CSV

## Project Structure

```text
Smart_Attendance_System/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
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
