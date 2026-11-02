"""User & Data Management System - main program (console menu)."""
from database import Database
from models import StudentManager, CourseManager, RecordManager
from validation import read_int, read_float


def show(rows, headers):
    """Print rows as a simple table."""
    if not rows:
        print("No results found.")
        return
    print("-" * 60)
    print(" | ".join(headers))
    print("-" * 60)
    for row in rows:
        print(" | ".join(str(x) for x in row))
    print("-" * 60)


def students_menu(students):
    while True:
        print("\n--- Students ---")
        print("1. Add  2. Delete  3. Update  4. Search  5. Show all  0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            print(students.add(input("Name: "), input("Email: "), read_int("Age: ")))
        elif choice == "2":
            print(students.delete(read_int("Student ID: ")))
        elif choice == "3":
            sid = read_int("Student ID: ")
            print(students.update(sid, input("New name: "), input("New email: "), read_int("New age: ")))
        elif choice == "4":
            show(students.search(input("Search word: ")), ["ID", "Name", "Email", "Age"])
        elif choice == "5":
            show(students.get_all(), ["ID", "Name", "Email", "Age"])
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def courses_menu(courses):
    while True:
        print("\n--- Courses ---")
        print("1. Add  2. Delete  3. Update  4. Search  5. Show all  0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            print(courses.add(input("Course name: ")))
        elif choice == "2":
            print(courses.delete(read_int("Course ID: ")))
        elif choice == "3":
            cid = read_int("Course ID: ")
            print(courses.update(cid, input("New name: ")))
        elif choice == "4":
            show(courses.search(input("Search word: ")), ["ID", "Course"])
        elif choice == "5":
            show(courses.get_all(), ["ID", "Course"])
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def records_menu(records):
    headers = ["ID", "Student", "Course", "Grade"]
    while True:
        print("\n--- Records (Grades) ---")
        print("1. Add  2. Delete  3. Update  4. Search  5. Show all  0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            sid = read_int("Student ID: ")
            cid = read_int("Course ID: ")
            print(records.add(sid, cid, read_float("Grade (0-100): ")))
        elif choice == "2":
            print(records.delete(read_int("Record ID: ")))
        elif choice == "3":
            rid = read_int("Record ID: ")
            print(records.update(rid, read_float("New grade (0-100): ")))
        elif choice == "4":
            show(records.search(input("Student or course name: ")), headers)
        elif choice == "5":
            show(records.get_all(), headers)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def main():
    db = Database()
    students, courses, records = StudentManager(db), CourseManager(db), RecordManager(db)
    while True:
        print("\n===== University Management System =====")
        print("1. Students")
        print("2. Courses")
        print("3. Records (Grades)")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            students_menu(students)
        elif choice == "2":
            courses_menu(courses)
        elif choice == "3":
            records_menu(records)
        elif choice == "0":
            print("Goodbye!")
            db.close()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
