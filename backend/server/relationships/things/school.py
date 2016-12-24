

class School:

    def __init__(self, name="", location="", instructors=[], subjects=[]):
        self.name = name
        self.location = location
        self.instructors = instructors
        self.subjects = subjects

    def encode(self):

        return {
            "name": self.name,
            "location": self.location,
            "instructors": [instructor.encode() for instructor in self.instructors],
            "subjects": [subject.encode() for subject in self.subjects]
        }
