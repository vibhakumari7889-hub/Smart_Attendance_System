import cv2
import shutil
from pathlib import Path

from src.database import add_student, delete_student


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "dataset" / "students"


def register_student():
    """Register a student and capture face samples."""

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()

    if not student_id or not name:
        print("Student ID and Name are required.")
        return

    # Check webcam before starting registration
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open webcam.")
        return

    student_folder = DATASET_DIR / student_id

    # Add student to database
    success, message = add_student(student_id, name)

    if not success:
        camera.release()
        print(message)
        return

    student_folder.mkdir(parents=True, exist_ok=True)

    print("\n" + message)
    print("Starting camera...")
    print("Look at the camera and keep your face clearly visible.")
    print("Press 'q' to stop capturing early.\n")

    cascade_path = (
        BASE_DIR
        / "models"
        / "haarcascade_frontalface_default.xml"
    )

    face_cascade = cv2.CascadeClassifier(str(cascade_path))

    if face_cascade.empty():
        camera.release()
        delete_student(student_id)
        shutil.rmtree(student_folder, ignore_errors=True)
        print("Error: Face detection model could not be loaded.")
        return

    sample_count = 0
    target_samples = 30

    try:
        while sample_count < target_samples:

            ret, frame = camera.read()

            if not ret:
                print("Error: Could not read frame from webcam.")
                break

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(100, 100)
            )

            for (x, y, w, h) in faces:

                sample_count += 1

                face_image = gray[
                    y:y + h,
                    x:x + w
                ]

                image_path = (
                    student_folder
                    / f"{sample_count}.jpg"
                )

                cv2.imwrite(
                    str(image_path),
                    face_image
                )

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Samples: {sample_count}/{target_samples}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                # Capture only one face per frame
                break

            cv2.imshow(
                "Student Registration - Face Capture",
                frame
            )

            key = cv2.waitKey(100) & 0xFF

            if key == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()

    # Registration completed successfully
    if sample_count >= target_samples:

        print("\nFace samples captured successfully!")
        print(f"Student: {name}")
        print(f"Student ID: {student_id}")
        print(f"Samples captured: {sample_count}")

    # Registration was incomplete
    else:

        print("\nRegistration incomplete.")
        print(f"Samples captured: {sample_count}/{target_samples}")

        # Remove incomplete student from database
        delete_student(student_id)

        # Remove incomplete dataset
        shutil.rmtree(
            student_folder,
            ignore_errors=True
        )

        print("Incomplete registration has been removed.")
        print("Please register the student again.")


if __name__ == "__main__":
    register_student()