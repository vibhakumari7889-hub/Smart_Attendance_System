import csv
from pathlib import Path

from src.database import get_attendance


BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)


def display_attendance():
    """Display attendance records in the terminal."""

    records = get_attendance()

    if not records:
        print("\nNo attendance records found.")
        return

    print("\n" + "=" * 70)
    print("                 ATTENDANCE REPORT")
    print("=" * 70)

    print(
        f"{'ID':<12}"
        f"{'NAME':<20}"
        f"{'DATE':<15}"
        f"{'TIME':<12}"
        f"{'STATUS':<10}"
    )

    print("-" * 70)

    for student_id, name, date, time, status in records:
        print(
            f"{student_id:<12}"
            f"{name:<20}"
            f"{date:<15}"
            f"{time:<12}"
            f"{status:<10}"
        )

    print("=" * 70)


def export_attendance_to_csv():
    """Export attendance records to a CSV file."""

    records = get_attendance()

    if not records:
        print("\nNo attendance records available for export.")
        return

    file_path = REPORTS_DIR / "attendance_report.csv"

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "Name",
            "Date",
            "Time",
            "Status"
        ])

        writer.writerows(records)

    print("\nAttendance report exported successfully.")
    print(f"File: {file_path}")


if __name__ == "__main__":
    display_attendance()
    export_attendance_to_csv()