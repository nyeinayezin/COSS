from app.database.connection import get_connection
from app.database.query_loader import load_queries
from app.domain.student import Student


class StudentRepository:

    def __init__(self):
        self.queries = load_queries("students.sql")

    def add(self, student):
        connection = get_connection()

        try:
            cursor = connection.execute(
                self.queries["insert_student"],
                (
                    student.first_name,
                    student.last_name,
                    student.status,
                ),
            )

            connection.commit()
            student.student_id = cursor.lastrowid

            return student

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

    def get_by_id(self, student_id):
        connection = get_connection()

        try:
            row = connection.execute(
                self.queries["get_student_by_id"],
                (student_id,),
            ).fetchone()

            if row is None:
                return None

            student = Student(
                row["student_id"],
                row["first_name"],
                row["last_name"],
            )
            student.status = row["status"]

            return student

        finally:
            connection.close()

    def search(self, search_term):
        connection = get_connection()

        try:
            pattern = f"%{search_term}%"

            rows = connection.execute(
                self.queries["search_students"],
                (pattern, pattern),
            ).fetchall()

            students = []

            for row in rows:
                student = Student(
                    row["student_id"],
                    row["first_name"],
                    row["last_name"],
                )

                student.status = row["status"]
                students.append(student)

            return students

        finally:
            connection.close()

    def update(self, student):
        connection = get_connection()

        try:
            cursor = connection.execute(
                self.queries["update_student"],
                (
                    student.first_name,
                    student.last_name,
                    student.status,
                    student.student_id,
                ),
            )

            connection.commit()
            return cursor.rowcount > 0

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

    def deactivate(self, student_id):
        connection = get_connection()

        try:
            cursor = connection.execute(
                self.queries["deactivate_student"],
                (student_id,),
            )

            connection.commit()
            return cursor.rowcount > 0

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

    def get_all(self):
        connection = get_connection()

        try:
            rows = connection.execute(
                self.queries["get_all_students"]
            ).fetchall()

            students = []

            for row in rows:
                student = Student(
                    row["student_id"],
                    row["first_name"],
                    row["last_name"]
                )
                student.status = row["status"]
                students.append(student)

            return students

        finally:
            connection.close()