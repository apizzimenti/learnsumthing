

class Instructor:

    def __init__(self, name="", school={}, courses=[], sections=[], messages=[]):
        self.name = name
        self.school = school
        self.courses = courses
        self.sections = sections
        self.messages = messages

    def encode(self):

        return {
            "name": self.name,
            "courses": [course.encode() for course in self.courses],
            "sections": [section.encode() for section in self.sections],
            "messages": [message.encode() for message in self.messages]
        }
