"""Database layer: creates the SQLite database and tables."""
import sqlite3


class Database:
    def __init__(self, path="university.db"):
        self.conn = sqlite3.connect(path)
        self.create_tables()
        self.add_default_courses()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            grade REAL NOT NULL,
            UNIQUE(student_id, course_id),
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id))""")
        self.conn.commit()

    def add_default_courses(self):
        # The three courses of the project
        for name in ("Databases", "Programming", "English"):
            self.conn.execute("INSERT OR IGNORE INTO courses (name) VALUES (?)", (name,))
        self.conn.commit()

    def run(self, query, params=()):
        """Run INSERT / UPDATE / DELETE and return number of affected rows."""
        cur = self.conn.execute(query, params)
        self.conn.commit()
        return cur.rowcount

    def fetch(self, query, params=()):
        """Run SELECT and return all rows."""
        return self.conn.execute(query, params).fetchall()

    def close(self):
        self.conn.close()
