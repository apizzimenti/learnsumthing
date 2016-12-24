

class Section:

    def __init__(self, period, instructor, posts=[], course={}):
        self.period = period
        self.instructor = instructor
        self.posts = posts
        self.course = course

    def encode(self):

        return {
            "period": self.period,
            "instructor": self.instructor.encode(),
            "posts": [post.encode() for post in self.posts],
        }
