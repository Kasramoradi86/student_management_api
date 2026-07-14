class StudentNotFoundException(Exception):
    def __init__(self,student_id):
        self.student_id = student_id

class ClassRoomNotFoundException(Exception):
    def __init__(self,classroom_id):
        self.classroom_id = classroom_id