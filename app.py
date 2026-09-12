import streamlit as st
import cv2
import numpy as np
from pathlib import Path
from datetime import datetime

from src.database import (
    initialize_database,
    add_student,
    get_all_students,
    get_attendance,
    mark_attendance
)
from src.recognition import train_model, load_model

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset" / "students"
MODELS_DIR = BASE_DIR / "models"

CASCADE_PATH = MODELS_DIR / "haarcascade_frontalface_default.xml"

DATASET_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

initialize_database()

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Attendance System",
    page_icon="📸",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📸 Smart Attendance System")
st.caption("Face Recognition Based Attendance Management System")

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Select an option",
    [
        "🏠 Dashboard",
        "👤 Register Student",
        "🧠 Train Model",
        "📸 Mark Attendance",
        "📊 Attendance Report",
        "👥 Registered Students"
    ]
)

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if menu == "🏠 Dashboard":

    st.header("Welcome to Smart Attendance System")

    students = get_all_students()
    attendance = get_attendance()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👥 Registered Students",
            len(students)
        )

    with col2:
        st.metric(
            "📋 Attendance Records",
            len(attendance)
        )

    today = datetime.now().strftime("%Y-%m-%d")

    today_records = [
        record for record in attendance
        if record[2] == today
    ]

    with col3:
        st.metric(
            "✅ Today's Attendance",
            len(today_records)
        )

    st.divider()

    st.subheader("System Features")

    st.write("""
    - 👤 Student registration
    - 📷 Face sample collection
    - 🧠 Face recognition model training
    - 📸 Automatic attendance marking
    - 📊 Attendance reports
    - 🗃️ SQLite database
    - 📄 Attendance records
    """)


# --------------------------------------------------
# REGISTER STUDENT
# --------------------------------------------------

elif menu == "👤 Register Student":

    st.header("👤 Register Student")

    student_id = st.text_input(
        "Student ID",
        placeholder="Enter student ID"
    )

    name = st.text_input(
        "Student Name",
        placeholder="Enter student name"
    )

    st.subheader("📷 Capture Face Samples")

    picture = st.camera_input(
        "Take a picture"
    )

    if picture is not None:

        image_bytes = picture.getvalue()

        image_array = np.frombuffer(
            image_bytes,
            np.uint8
        )

        frame = cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR
        )

        if frame is not None:

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            face_cascade = cv2.CascadeClassifier(
                str(CASCADE_PATH)
            )

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(100, 100)
            )

            if len(faces) == 0:

                st.error(
                    "No face detected. Please capture another image."
                )

            else:

                if not student_id or not name:

                    st.warning(
                        "Please enter Student ID and Student Name first."
                    )

                else:

                    student_folder = (
                        DATASET_DIR / student_id
                    )

                    student_folder.mkdir(
                        parents=True,
                        exist_ok=True
                    )

                    success, message = add_student(
                        student_id,
                        name
                    )

                    if not success:

                        st.warning(message)

                    else:

                        x, y, w, h = faces[0]

                        face_image = gray[
                            y:y + h,
                            x:x + w
                        ]

                        existing_samples = list(
                            student_folder.glob("*.jpg")
                        )

                        sample_number = (
                            len(existing_samples) + 1
                        )

                        image_path = (
                            student_folder /
                            f"{sample_number}.jpg"
                        )

                        cv2.imwrite(
                            str(image_path),
                            face_image
                        )

                        st.success(
                            f"Face sample {sample_number} captured successfully!"
                        )

                        st.info(
                            "Capture multiple images with slightly different "
                            "angles/expressions for better recognition."
                        )


# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------

elif menu == "🧠 Train Model":

    st.header("🧠 Train Face Recognition Model")

    students = get_all_students()

    if not students:

        st.warning(
            "No students registered yet. Please register a student first."
        )

    else:

        st.write(
            f"Registered students: **{len(students)}**"
        )

        if st.button(
            "🚀 Train Recognition Model",
            use_container_width=True
        ):

            with st.spinner(
                "Training face recognition model..."
            ):

                success = train_model()

            if success:

                st.success(
                    "Face recognition model trained successfully! 🎉"
                )

            else:

                st.error(
                    "Model training failed. Make sure face samples exist."
                )


# --------------------------------------------------
# MARK ATTENDANCE
# --------------------------------------------------

elif menu == "📸 Mark Attendance":

    st.header("📸 Mark Attendance")

    st.write(
        "Allow camera access and capture your face."
    )

    picture = st.camera_input(
        "Capture face for attendance"
    )

    if picture is not None:

        recognizer, label_map = load_model()

        if recognizer is None:

            st.error(
                "Recognition model not found. "
                "Please register students and train the model first."
            )

        else:

            image_bytes = picture.getvalue()

            image_array = np.frombuffer(
                image_bytes,
                np.uint8
            )

            frame = cv2.imdecode(
                image_array,
                cv2.IMREAD_COLOR
            )

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            face_cascade = cv2.CascadeClassifier(
                str(CASCADE_PATH)
            )

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(100, 100)
            )

            if len(faces) == 0:

                st.error(
                    "No face detected. Please try again."
                )

            else:

                recognized = False

                for (x, y, w, h) in faces:

                    face_region = gray[
                        y:y + h,
                        x:x + w
                    ]

                    label, confidence = (
                        recognizer.predict(face_region)
                    )

                    if (
                        confidence < 70
                        and str(label) in label_map
                    ):

                        student = label_map[str(label)]

                        student_id = student["student_id"]
                        name = student["name"]

                        success, message = mark_attendance(
                            student_id,
                            name
                        )

                        st.image(
                            cv2.cvtColor(
                                frame,
                                cv2.COLOR_BGR2RGB
                            ),
                            caption=f"Recognized: {name}"
                        )

                        if success:

                            st.success(
                                f"✅ Attendance marked for {name}"
                            )

                        else:

                            st.info(
                                f"ℹ️ {message}"
                            )

                        recognized = True
                        break

                if not recognized:

                    st.error(
                        "❌ Face not recognized."
                    )


# --------------------------------------------------
# ATTENDANCE REPORT
# --------------------------------------------------

elif menu == "📊 Attendance Report":

    st.header("📊 Attendance Report")

    records = get_attendance()

    if not records:

        st.info(
            "No attendance records found."
        )

    else:

        data = []

        for student_id, name, date, time, status in records:

            data.append(
                {
                    "Student ID": student_id,
                    "Name": name,
                    "Date": date,
                    "Time": time,
                    "Status": status
                }
            )

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )

        csv_data = "\n".join(
            [
                "Student ID,Name,Date,Time,Status"
            ]
            + [
                f"{row['Student ID']},{row['Name']},"
                f"{row['Date']},{row['Time']},{row['Status']}"
                for row in data
            ]
        )

        st.download_button(
            "⬇️ Download Attendance CSV",
            csv_data,
            file_name="attendance_report.csv",
            mime="text/csv",
            use_container_width=True
        )


# --------------------------------------------------
# REGISTERED STUDENTS
# --------------------------------------------------

elif menu == "👥 Registered Students":

    st.header("👥 Registered Students")

    students = get_all_students()

    if not students:

        st.info(
            "No students registered yet."
        )

    else:

        data = []

        for student_id, name, created_at in students:

            data.append(
                {
                    "Student ID": student_id,
                    "Name": name,
                    "Registered On": created_at
                }
            )

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )