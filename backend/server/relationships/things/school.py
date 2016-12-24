

class School:

    def __init__(self, name="", location="", instructors=[], subjects=[], students=[]):
        self.name = name
        self.location = location
        self.instructors = instructors
        self.subjects = subjects
        self.students = students

    def encode(self):

        return {
            "name": self.name,
            "location": self.location,
            "instructors": [instructor.encode() for instructor in self.instructors],
            "subjects": [subject.encode() for subject in self.subjects],
            "students": [student.encode() for student in self.students]
        }
