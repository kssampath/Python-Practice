class Student:
    def __init__(self, studnet_id, name, marks):
        self.student_id = studnet_id
        self.name = name
        self.marks = marks
        
    def average_marks(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        return total / len(self.marks)
    
    def has_passed(self):
        return all(mark >= 40 for mark in self.marks.values())
class School:
    def __init__(self):
        self.students = []
    def add_students(self, student):
        self.students.append(student)
    def top_student(self):
        return list(filter(lambda student: student.average_marks() >=80, self.students))
    def failed_students(self):
        return list(filter(lambda student: not student.has_passed(), self.students))
    def subject_topper(self, subject):
        return max(self.students, key=lambda s: s.marks[subject])


    