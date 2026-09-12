import sqlite3
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "attendance.db"

DATABASE_DIR.mkdir(exist_ok=True)


def get_connection():
    """Create and return a SQLite database connection."""
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Create all required database tables."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            status TEXT DEFAULT 'Present',
            UNIQUE(student_id, date)
        )
    """)

    conn.commit()
    conn.close()


def add_student(student_id, name):
    """Add a new student to the database."""

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO students (student_id, name, created_at)
            VALUES (?, ?, ?)
        """, (
            student_id,
            name,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()

        return True, "Student registered successfully."

    except sqlite3.IntegrityError:
        return False, "Student ID already exists."

    finally:
        conn.close()


def get_student(student_id):
    """Get a student by student ID."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    return student


def get_all_students():
    """Return all registered students."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, created_at
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    conn.close()

    return students


def mark_attendance(student_id, name):
    """Mark attendance only once per student per day."""

    now = datetime.now()

    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO attendance
            (student_id, name, date, time, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            student_id,
            name,
            date,
            time,
            "Present"
        ))

        conn.commit()

        return True, f"Attendance marked for {name}."

    except sqlite3.IntegrityError:
        return False, f"{name}'s attendance is already marked today."

    finally:
        conn.close()


def get_attendance():
    """Return all attendance records."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, date, time, status
        FROM attendance
        ORDER BY date DESC, time DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return records


def delete_student(student_id):
    """Delete a student only when needed."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted > 0