class Enrolment:
    def __init__(self, student, class_group):
        self.student = student
        self.class_group = class_group
        self.status = "ACTIVE"

    def cancel(self):
        if self.status == "CANCELLED":
            raise ValueError("Enrolment is already cancelled")

        self.status = "CANCELLED"

    def is_active(self):
        return self.status == "ACTIVE"