
class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.status = "ACTIVE"

    def update_details(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def deactivate(self):
        self.status = "INACTIVE"

    def activate(self):
        self.status = "ACTIVE"