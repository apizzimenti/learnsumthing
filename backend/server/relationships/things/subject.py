

class Subject:

    def __init__(self, name="", school={}, courses=[], instructors=[]):
        self.name = name
        self.school = school
        self.courses = courses
        self.instructors = instructors

    def encode(self):

        return {
            "name": self.name,
            "courses": [course.encode() for course in self.courses],
            "instructors": [instructor.encode() for instructor in self.instructors]
        }
