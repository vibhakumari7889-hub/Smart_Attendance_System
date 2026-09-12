from src.database import initialize_database, get_all_students
from src.registration import register_student
from src.recognition import train_model, recognize_faces
from src.reports import display_attendance, export_attendance_to_csv


def display_students():
    """Display all registered students."""

    students = get_all_students()

    if not students:
        print("\nNo students registered yet.")
        return

    print("\n" + "=" * 60)
    print("                 REGISTERED STUDENTS")
    print("=" * 60)

    print(
        f"{'ID':<15}"
        f"{'NAME':<25}"
        f"{'REGISTERED ON':<20}"
    )

    print("-" * 60)

    for student_id, name, created_at in students:
        print(
            f"{student_id:<15}"
            f"{name:<25}"
            f"{created_at:<20}"
        )

    print("=" * 60)


def show_menu():
    """Display the main menu."""

    print("\n")
    print("=" * 60)
    print("              SMART ATTENDANCE SYSTEM")
    print("=" * 60)

    print("1. Register Student")
    print("2. Train Face Recognition Model")
    print("3. Start Attendance")
    print("4. View Attendance Report")
    print("5. Export Attendance to CSV")
    print("6. View Registered Students")
    print("7. Exit")

    print("=" * 60)


def main():
    """Main application function."""

    initialize_database()

    print("\nDatabase initialized successfully.")
    print("Welcome to Smart Attendance System!")

    while True:

        show_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":

            print("\n--- Student Registration ---")
            register_student()

        elif choice == "2":

            print("\n--- Training Face Recognition Model ---")
            train_model()

        elif choice == "3":

            print("\n--- Starting Attendance System ---")
            recognize_faces()

        elif choice == "4":

            print("\n--- Attendance Report ---")
            display_attendance()

        elif choice == "5":

            print("\n--- Export Attendance ---")
            export_attendance_to_csv()

        elif choice == "6":

            display_students()

        elif choice == "7":

            print("\nThank you for using Smart Attendance System!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice.")
            print("Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()