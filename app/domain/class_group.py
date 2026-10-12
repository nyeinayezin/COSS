class ClassGroup:
    def __init__(self, class_id, name, capacity):
        self.class_id = class_id
        self.name = name
        self.capacity = capacity
        self.current_students = 0

    def has_available_place(self):
        return self.current_students < self.capacity

    def add_student(self):
        if not self.has_available_place():
            raise ValueError("Class is full")

        self.current_students += 1

    def remove_student(self):
        if self.current_students > 0:
            self.current_students -= 1