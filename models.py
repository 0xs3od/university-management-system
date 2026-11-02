"""Classes (OOP): each class manages one part of the system."""
from validation import is_valid_name, is_valid_email, is_valid_age, is_valid_grade


class StudentManager:
    def __init__(self, db):
        self.db = db

    def add(self, name, email, age):
        if not is_valid_name(name):
            return "Error: name must be letters only (at least 3 characters)."
        if not is_valid_email(email):
            return "Error: invalid email."
        if not is_valid_age(age):
            return "Error: age must be between 16 and 60."
        if self.db.fetch("SELECT id FROM students WHERE email = ?", (email,)):
            return "Error: this email already exists."
        self.db.run("INSERT INTO students (name, email, age) VALUES (?, ?, ?)",
                    (name.strip(), email.strip(), age))
        return "Student added successfully."

    def delete(self, student_id):
        self.db.run("DELETE FROM records WHERE student_id = ?", (student_id,))
        if self.db.run("DELETE FROM students WHERE id = ?", (student_id,)) == 0:
            return "Error: student not found."
        return "Student deleted."

    def update(self, student_id, name, email, age):
        if not self.db.fetch("SELECT id FROM students WHERE id = ?", (student_id,)):
            return "Error: student not found."
        if not is_valid_name(name):
            return "Error: invalid name."
        if not is_valid_email(email):
            return "Error: invalid email."
        if not is_valid_age(age):
            return "Error: age must be between 16 and 60."
        if self.db.fetch("SELECT id FROM students WHERE email = ? AND id != ?", (email, student_id)):
            return "Error: this email belongs to another student."
        self.db.run("UPDATE students SET name = ?, email = ?, age = ? WHERE id = ?",
                    (name.strip(), email.strip(), age, student_id))
        return "Student updated."

    def search(self, word):
        return self.db.fetch(
            "SELECT id, name, email, age FROM students WHERE name LIKE ? OR email LIKE ?",
            (f"%{word}%", f"%{word}%"))

    def get_all(self):
        return self.db.fetch("SELECT id, name, email, age FROM students")


class CourseManager:
    def __init__(self, db):
        self.db = db

    def add(self, name):
        name = name.strip()
        if len(name) < 2:
            return "Error: course name is too short."
        if self.db.fetch("SELECT id FROM courses WHERE name = ? COLLATE NOCASE", (name,)):
            return "Error: course already exists."
        self.db.run("INSERT INTO courses (name) VALUES (?)", (name,))
        return "Course added."

    def delete(self, course_id):
        self.db.run("DELETE FROM records WHERE course_id = ?", (course_id,))
        if self.db.run("DELETE FROM courses WHERE id = ?", (course_id,)) == 0:
            return "Error: course not found."
        return "Course deleted."

    def update(self, course_id, name):
        name = name.strip()
        if len(name) < 2:
            return "Error: course name is too short."
        if self.db.run("UPDATE courses SET name = ? WHERE id = ?", (name, course_id)) == 0:
            return "Error: course not found."
        return "Course updated."

    def search(self, word):
        return self.db.fetch("SELECT id, name FROM courses WHERE name LIKE ?", (f"%{word}%",))

    def get_all(self):
        return self.db.fetch("SELECT id, name FROM courses")


class RecordManager:
    def __init__(self, db):
        self.db = db

    def add(self, student_id, course_id, grade):
        if not self.db.fetch("SELECT id FROM students WHERE id = ?", (student_id,)):
            return "Error: student not found."
        if not self.db.fetch("SELECT id FROM courses WHERE id = ?", (course_id,)):
            return "Error: course not found."
        if not is_valid_grade(grade):
            return "Error: grade must be between 0 and 100."
        if self.db.fetch("SELECT id FROM records WHERE student_id = ? AND course_id = ?",
                         (student_id, course_id)):
            return "Error: this student already has a grade in this course."
        self.db.run("INSERT INTO records (student_id, course_id, grade) VALUES (?, ?, ?)",
                    (student_id, course_id, grade))
        return "Record added."

    def delete(self, record_id):
        if self.db.run("DELETE FROM records WHERE id = ?", (record_id,)) == 0:
            return "Error: record not found."
        return "Record deleted."

    def update(self, record_id, grade):
        if not is_valid_grade(grade):
            return "Error: grade must be between 0 and 100."
        if self.db.run("UPDATE records SET grade = ? WHERE id = ?", (grade, record_id)) == 0:
            return "Error: record not found."
        return "Record updated."

    def search(self, word):
        """Search records by student name or course name."""
        return self.db.fetch(self._select() + " WHERE s.name LIKE ? OR c.name LIKE ?",
                             (f"%{word}%", f"%{word}%"))

    def get_all(self):
        return self.db.fetch(self._select())

    @staticmethod
    def _select():
        return """SELECT r.id, s.name, c.name, r.grade
                 FROM records r
                 JOIN students s ON s.id = r.student_id
                 JOIN courses c ON c.id = r.course_id"""
