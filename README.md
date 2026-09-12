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
ote: Face datasets, SQLite database files, trained models, and generated reports are stored locally and excluded from GitHub using .gitignore.

How It Works
Register a student using their Student ID and Name.
The webcam captures multiple face samples.
Face samples are stored locally for training.
Train the LBPH face recognition model.
Start the attendance system.
The webcam detects and recognizes registered students.
Attendance is automatically recorded in SQLite.
Duplicate attendance for the same student on the same day is prevented.
Attendance records can be viewed or exported as a CSV report.
Installation
1. Clone the Repository
git clone https://github.com/vibhakumari7889-hub/Smart_Attendance_System.git
cd Smart_Attendance_System
2. Create a Virtual Environment
python -m venv .venv
3. Activate the Virtual Environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
Run the Application
python main.py
Main Menu
1. Register Student
2. Train Face Recognition Model
3. Start Attendance
4. View Attendance Report
5. Export Attendance to CSV
6. View Registered Students
7. Exit
Database

The system uses SQLite to store:

Student information
Attendance records
Attendance date and time
Attendance status
Attendance Reports

Attendance records can be exported as:

reports/attendance_report.csv
Privacy Note

Face images and generated biometric-related data are stored locally. These files are intentionally excluded from the public GitHub repository using .gitignore.

Future Improvements
Graphical User Interface (GUI)
Admin authentication
Attendance percentage calculation
Monthly attendance statistics
Email notifications
Cloud database integration
Web-based attendance dashboard
Author

Vibha Kumari

B.Tech Information Technology Student

Built using Python, OpenCV, and SQLite.


**Important:** आखिरी ``` भी paste करना है।

फिर **Ctrl + S** दबाकर save करो और मुझे `done` लिखो।
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


text
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

हाँ 👍 अब तक बिल्कुल सही है। तुम्हारा Project Structure वाला हिस्सा भी अब proper code block में है।

लेकिन तुमने अभी README आधा ही paste किया है — __init__.py के बाद बाकी content बाकी है।

अब उसी के नीचे बाकी यह पूरा हिस्सा paste करो:

Note: Face datasets, SQLite database files, trained models, and generated reports are stored locally and excluded from GitHub using .gitignore.

How It Works
1.Register a student using their Student ID and Name.
2.The webcam captures multiple face samples.
3.Face samples are stored locally for training.
4.Train the LBPH face recognition model.
5.Start the attendance system.
6.The webcam detects and recognizes registered students.
7.Attendance is automatically recorded in SQLite.
8.Duplicate attendance for the same student on the same day is prevented.
9.Attendance records can be viewed or exported as a CSV report.
Installation
1. Clone the Repository
git clone https://github.com/vibhakumari7889-hub/Smart_Attendance_System.git
cd Smart_Attendance_System
2. Create a Virtual Environment
python -m venv .venv
3. Activate the Virtual Environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
Run the Application
python main.py
Main Menu
1. Register Student
2. Train Face Recognition Model
3. Start Attendance
4. View Attendance Report
5. Export Attendance to CSV
6. View Registered Students
7. Exit
Database

The system uses SQLite to store:

Student information
Attendance records
Attendance date and time
Attendance status
Attendance Reports

Attendance records can be exported as:

reports/attendance_report.csv
Privacy Note

Face images and generated biometric-related data are stored locally. These files are intentionally excluded from the public GitHub repository using .gitignore.

Future Improvements
Graphical User Interface (GUI)
Admin authentication
Attendance percentage calculation
Monthly attendance statistics
Email notifications
Cloud database integration
Web-based attendance dashboard
Author

Vibha Kumari

B.Tech Information Technology Student

Built using Python, OpenCV,and SQLite.
