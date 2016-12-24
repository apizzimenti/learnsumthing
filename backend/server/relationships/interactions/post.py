

class Post:

    def __init__(self, body, author, course=None, section=None, comments=[], votes=[0, 0]):
        self.body = body
        self.author = author
        self.course = course
        self.section = section
        self.comments = comments
        self.votes = votes

    def encode(self):

        d = {
            "body": self.body,
            "votes": self.votes,
            "author": self.author.encode(),
            "comments": [comment.encode() for comment in self.comments]
        }

        if self.section:
            d["section"] = self.section.encode()
        else:
            d["course"] = self.course.encode()
