import cv2
import json
import numpy as np
from pathlib import Path

from src.database import get_all_students
from src.attendance import record_attendance


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "dataset" / "students"
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "face_model.yml"
LABEL_MAP_PATH = MODELS_DIR / "label_map.json"


def train_model():
    """Train the LBPH face recognition model."""

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    students = get_all_students()

    if not students:
        print("No students registered yet.")
        return False

    faces = []
    labels = []
    label_map = {}

    current_label = 0

    for student_id, name, _ in students:

        student_folder = DATASET_DIR / student_id

        if not student_folder.exists():
            print(f"Dataset not found for {name} ({student_id}).")
            continue

        image_files = list(student_folder.glob("*.jpg"))

        if not image_files:
            print(f"No face images found for {name} ({student_id}).")
            continue

        student_images_added = 0

        for image_path in image_files:

            image = cv2.imread(
                str(image_path),
                cv2.IMREAD_GRAYSCALE
            )

            if image is None:
                continue

            faces.append(image)
            labels.append(current_label)
            student_images_added += 1

        if student_images_added > 0:

            label_map[str(current_label)] = {
                "student_id": student_id,
                "name": name
            }

            current_label += 1

    if not faces:
        print("No face images available for training.")
        return False

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.train(
        faces,
        np.array(labels)
    )

    recognizer.write(str(MODEL_PATH))

    with open(
        LABEL_MAP_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            label_map,
            file,
            indent=4
        )

    print("\nFace recognition model trained successfully.")
    print(f"Students used for training: {current_label}")
    print(f"Model saved at: {MODEL_PATH}")

    return True


def load_model():
    """Load the trained face recognition model."""

    if not MODEL_PATH.exists():

        print("Face recognition model not found.")
        print("Please train the model first.")

        return None, None

    if not LABEL_MAP_PATH.exists():

        print("Label mapping file not found.")

        return None, None

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read(
        str(MODEL_PATH)
    )

    with open(
        LABEL_MAP_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        label_map = json.load(file)

    return recognizer, label_map


def show_success_screen(
    window_name,
    frame,
    name,
    student_id,
    already_marked=False
):
    """Show attendance confirmation screen."""

    confirmation_frame = frame.copy()

    height, width = confirmation_frame.shape[:2]

    # Dark overlay
    overlay = confirmation_frame.copy()

    cv2.rectangle(
        overlay,
        (0, 0),
        (width, height),
        (0, 0, 0),
        -1
    )

    confirmation_frame = cv2.addWeighted(
        overlay,
        0.65,
        confirmation_frame,
        0.35,
        0
    )

    # Draw a large green check mark
    center_x = width // 2
    center_y = height // 2 - 70

    cv2.line(
        confirmation_frame,
        (center_x - 70, center_y),
        (center_x - 20, center_y + 50),
        (0, 255, 0),
        10
    )

    cv2.line(
        confirmation_frame,
        (center_x - 20, center_y + 50),
        (center_x + 80, center_y - 70),
        (0, 255, 0),
        10
    )

    if already_marked:

        message = "ATTENDANCE ALREADY MARKED"

    else:

        message = "ATTENDANCE MARKED"

    text_size = cv2.getTextSize(
        message,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        2
    )[0]

    text_x = (width - text_size[0]) // 2

    cv2.putText(
        confirmation_frame,
        message,
        (text_x, center_y + 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2
    )

    student_text = f"{name}  |  ID: {student_id}"

    student_size = cv2.getTextSize(
        student_text,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        2
    )[0]

    student_x = (width - student_size[0]) // 2

    cv2.putText(
        confirmation_frame,
        student_text,
        (student_x, center_y + 175),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        confirmation_frame,
        "Camera closing automatically...",
        (width // 2 - 180, height - 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1
    )

    cv2.imshow(
        window_name,
        confirmation_frame
    )

    # Keep confirmation screen visible for 2 seconds
    cv2.waitKey(2000)


def recognize_faces():
    """Recognize registered students and mark attendance."""

    recognizer, label_map = load_model()

    if recognizer is None:
        return

    cascade_path = (
        BASE_DIR
        / "models"
        / "haarcascade_frontalface_default.xml"
    )

    face_cascade = cv2.CascadeClassifier(
        str(cascade_path)
    )

    if face_cascade.empty():

        print(
            "Error: Face detection model could not be loaded."
        )

        return

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():

        print("Error: Could not open webcam.")

        return

    # Camera initialization
    for _ in range(10):
        camera.read()

    window_name = "Smart Attendance - Face Recognition"

    cv2.namedWindow(
        window_name,
        cv2.WINDOW_NORMAL
    )

    print("\nStarting face recognition...")
    print("Look at the camera.")
    print("Attendance will be marked automatically.")
    print("Camera will close automatically after recognition.\n")

    attendance_completed = False

    try:

        while True:

            ret, frame = camera.read()

            if not ret:

                print("Could not read webcam frame.")
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

                face_region = gray[
                    y:y + h,
                    x:x + w
                ]

                label, confidence = recognizer.predict(
                    face_region
                )

                if (
                    confidence < 70
                    and str(label) in label_map
                ):

                    student = label_map[str(label)]

                    student_id = student["student_id"]
                    name = student["name"]

                    # Mark attendance
                    success = record_attendance(
                        student_id,
                        name
                    )

                    # Show confirmation screen
                    show_success_screen(
                        window_name,
                        frame,
                        name,
                        student_id,
                        already_marked=not success
                    )

                    attendance_completed = True

                    break

                else:

                    # Unknown face
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w, y + h),
                        (0, 0, 255),
                        2
                    )

                    cv2.putText(
                        frame,
                        "Unknown",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2
                    )

            if attendance_completed:

                break

            # Instruction
            cv2.putText(
                frame,
                "Look at camera",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            cv2.imshow(
                window_name,
                frame
            )

            key = cv2.waitKey(10) & 0xFF

            if (
                key == ord("q")
                or key == ord("Q")
                or key == 27
            ):

                break

            # Detect manual window close
            try:

                if cv2.getWindowProperty(
                    window_name,
                    cv2.WND_PROP_VISIBLE
                ) < 1:

                    break

            except cv2.error:

                break

    finally:

        camera.release()

        cv2.destroyAllWindows()

        for _ in range(3):
            cv2.waitKey(1)

    print("\nAttendance session completed.")


if __name__ == "__main__":
    recognize_faces()