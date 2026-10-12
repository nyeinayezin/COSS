from app.domain.student import Student
from app.repositories.student_repository import StudentRepository


class StudentService:

    def __init__(self, student_repository=None):
        self.student_repository = (
            student_repository or StudentRepository()
        )

    def register_student(self, first_name, last_name):
        first_name = first_name.strip()
        last_name = last_name.strip()

        if not first_name:
            raise ValueError("First name is required")

        if not last_name:
            raise ValueError("Last name is required")

        student = Student(
            None,
            first_name,
            last_name
        )

        return self.student_repository.add(student)

    def get_student(self, student_id):
        return self.student_repository.get_by_id(student_id)

    def search_students(self, search_term=""):
        search_term = search_term.strip()

        if not search_term:
            return self.student_repository.get_all()

        return self.student_repository.search(search_term)

    def update_student(self, student_id, first_name, last_name):
        student = self.student_repository.get_by_id(student_id)

        if student is None:
            raise ValueError("Student not found")

        first_name = first_name.strip()
        last_name = last_name.strip()

        if not first_name:
            raise ValueError("First name is required")

        if not last_name:
            raise ValueError("Last name is required")

        student.update_details(first_name, last_name)

        if not self.student_repository.update(student):
            raise ValueError("Unable to update student")

        return student

    def deactivate_student(self, student_id):
        student = self.student_repository.get_by_id(student_id)

        if student is None:
            raise ValueError("Student not found")

        if student.status == "INACTIVE":
            raise ValueError("Student is already inactive")

        if not self.student_repository.deactivate(student_id):
            raise ValueError("Unable to deactivate student")

        student.deactivate()
        return student