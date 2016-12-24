

class Course:

    def __init__(self, title, school={}, subject={}, instructors=[], sections=[], posts=[]):
        self.title = title
        self.school = school
        self.subject = subject
        self.instructors = instructors
        self.sections = sections
        self.posts = posts

    def encode(self):

        return {
            "title": self.title,
            "instructors": [instructor.encode() for instructor in self.instructors],
            "sections": [section.encode() for section in self.sections],
            "posts": [post.encode() for post in self.posts]
        }
