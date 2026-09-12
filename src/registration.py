import cv2
from pathlib import Path

from src.database import add_student


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "dataset" / "students"


def register_student():
    """Register a student and capture face samples."""

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()

    if not student_id or not name:
        print("Student ID and Name are required.")
        return

    # Check webcam before creating the registration
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open webcam.")
        return

    # Create student's dataset folder
    student_folder = DATASET_DIR / student_id
    student_folder.mkdir(parents=True, exist_ok=True)

    # Add student to database
    success, message = add_student(student_id, name)

    if not success:
        camera.release()
        print(message)
        return

    print("\n" + message)
    print("Starting camera...")
    print("Look at the camera and keep your face clearly visible.")
    print("Press 'q' to stop capturing early.\n")

    face_cascade = cv2.CascadeClassifier(
    str(BASE_DIR / "models" / "haarcascade_frontalface_default.xml")
)

    sample_count = 0
    target_samples = 30

    while sample_count < target_samples:

        ret, frame = camera.read()

        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(100, 100)
        )

        for (x, y, w, h) in faces:

            sample_count += 1

            face_image = gray[y:y + h, x:x + w]

            image_path = student_folder / f"{sample_count}.jpg"

            cv2.imwrite(str(image_path), face_image)

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

    camera.release()
    cv2.destroyAllWindows()

    if sample_count >= target_samples:
        print("\nFace samples captured successfully!")
        print(f"Student: {name}")
        print(f"Student ID: {student_id}")
        print(f"Samples captured: {sample_count}")
    else:
        print("\nRegistration stopped.")
        print(f"Samples captured: {sample_count}/{target_samples}")


if __name__ == "__main__":
    register_student()