# Name: Yelnur Akhmetzhan
# Group: SE-2504
# Project: Student Grade & Attendance Tracker

from services.tracker import Tracker


# TASK 1: Show menu
# This function prints all options for the user.
def show_menu():
    print("\n===== Student Grade & Attendance Tracker =====")
    print("1. Add student")
    print("2. Edit student")
    print("3. Delete student")
    print("4. Search student")
    print("5. Add grade")
    print("6. Mark attendance")
    print("7. Show all students")
    print("8. Show low average students")
    print("9. Show low attendance students")
    print("10. Show all subjects")
    print("11. Save data")
    print("12. Load data")
    print("0. Exit")


# TASK 2: Print student list
# This function is used to display search results or reports.
def print_students(students):
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student)


# TASK 3: Main program execution
# The main function controls the whole menu-based program.
def main():
    tracker = Tracker()
    tracker.load_data()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")

            if tracker.add_student(student_id, name):
                print("Student added successfully.")
            else:
                print("Student with this ID already exists.")

        elif choice == "2":
            student_id = input("Enter student ID: ")
            new_name = input("Enter new name: ")

            if tracker.edit_student(student_id, new_name):
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif choice == "3":
            student_id = input("Enter student ID: ")

            if tracker.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            keyword = input("Enter name or ID: ")
            results = tracker.search_student(keyword)
            print_students(results)

        elif choice == "5":
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")

            try:
                grade = float(input("Enter grade: "))
                if tracker.add_grade(student_id, subject, grade):
                    print("Grade added successfully.")
                else:
                    print("Student not found.")
            except ValueError:
                print("Grade must be a number.")

        elif choice == "6":
            student_id = input("Enter student ID: ")
            date = input("Enter date (example: 2026-05-21): ")
            status = input("Enter status (present/absent): ").lower()

            if status == "present" or status == "absent":
                if tracker.mark_attendance(student_id, date, status):
                    print("Attendance marked successfully.")
                else:
                    print("Student not found.")
            else:
                print("Status must be present or absent.")

        elif choice == "7":
            students = tracker.show_all_students()
            print_students(students)

        elif choice == "8":
            try:
                limit = float(input("Enter average grade limit: "))
                students = tracker.get_low_average_students(limit)
                print_students(students)
            except ValueError:
                print("Limit must be a number.")

        elif choice == "9":
            try:
                limit = float(input("Enter attendance percentage limit: "))
                students = tracker.get_low_attendance_students(limit)
                print_students(students)
            except ValueError:
                print("Limit must be a number.")

        elif choice == "10":
            subjects = tracker.get_all_subjects()

            if len(subjects) == 0:
                print("No subjects found.")
            else:
                print("Subjects:")
                for subject in subjects:
                    print("-", subject)

        elif choice == "11":
            tracker.save_data()
            print("Data saved successfully.")

        elif choice == "12":
            tracker.load_data()
            print("Data loaded successfully.")

        elif choice == "0":
            tracker.save_data()
            print("Data saved. Program closed.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
