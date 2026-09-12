from src.database import mark_attendance


def record_attendance(student_id, name):
    """Record attendance for a recognized student."""

    success, message = mark_attendance(
        student_id,
        name
    )

    print(message)

    return success


if __name__ == "__main__":
    print("Attendance module is ready.")