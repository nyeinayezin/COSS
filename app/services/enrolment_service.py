
from app.domain.enrolment import Enrolment


class EnrolmentService:

    def __init__(self):
        self.enrolments = []

    def enrol_student(self, student, class_group):

        for enrolment in self.enrolments:
            if (
                enrolment.student.student_id == student.student_id
                and enrolment.class_group.class_id == class_group.class_id
                and enrolment.is_active()
            ):
                raise ValueError(
                    "Student is already enrolled in this class"
                )

        if not class_group.has_available_place():
            raise ValueError("Class is full")

        class_group.add_student()

        enrolment = Enrolment(student, class_group)

        self.enrolments.append(enrolment)

        return enrolment

    def cancel_enrolment(self, enrolment):

        if not enrolment.is_active():
            raise ValueError("Enrolment is already cancelled")

        enrolment.cancel()
        enrolment.class_group.remove_student()