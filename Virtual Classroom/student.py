from participant import Participant


class Student(Participant):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
