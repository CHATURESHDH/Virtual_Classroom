from participant import Participant
from classroom import Classroom
from student import Student
from assignment import Assignment


class VirtualClassroomManager:
    def __init__(self):
        self._classrooms = {}

    def add_classroom(self, class_name):
        if class_name not in self._classrooms:
            self._classrooms[class_name] = Classroom(class_name)
            print(f'Classroom "{class_name}" has been created.')
        else:
            print(f'Classroom "{class_name}" already exists.')

    def add_student(self, student_id, class_name):
        if class_name not in self._classrooms:
            print(f'Error: Classroom "{class_name}" does not exist.')
        else:
            student = Student(student_id, f"Student {student_id}")
            self._classrooms[class_name].add_student(student)
            print(f'Student "{student_id}" has been enrolled in "{class_name}".')

    def list_students(self, class_name):
        if class_name not in self._classrooms:
            print(f'Error: Classroom "{class_name}" does not exist.')
        else:
            students = self._classrooms[class_name].list_students()
            if students:
                print(
                    f'Students enrolled in "{class_name}": {[student.get_id() for student in students]}'
                )
            else:
                print(f'No students enrolled in "{class_name}".')

    def schedule_assignment(self, class_name, assignment_details):
        if class_name not in self._classrooms:
            print(f'Error: Classroom "{class_name}" does not exist.')
        else:
            assignment = Assignment(class_name, assignment_details)
            self._classrooms[class_name].schedule_assignment(assignment)
            print(f'Assignment for "{class_name}" has been scheduled.')

    def submit_assignment(self, student_id, class_name, assignment_details):
        print(f'Assignment submitted by Student "{student_id}" in "{class_name}".')
