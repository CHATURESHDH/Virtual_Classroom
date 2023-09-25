class Classroom:
    def __init__(self, class_name):
        self._class_name = class_name
        self._students = set()
        self._assignments = []

    def add_student(self, student):
        self._students.add(student)

    def list_students(self):
        return self._students

    def schedule_assignment(self, details):
        self._assignments.append(details)
