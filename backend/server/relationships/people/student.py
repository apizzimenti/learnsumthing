

class Student:

    def __init__(self, name="", school={}, sections=[], votes=[0, 0], posts=[], comments=[], messages=[], bio={}):
        self.name = name
        self.school = school
        self.sections = sections
        self.votes = votes
        self.posts = posts
        self.comments = comments
        self.messages = messages
        self.bio = bio

    def encode(self):

        return {
            "name": self.name,
            "sections": [section.encode() for section in self.sections],
            "votes": self.votes,
            "posts": [post.encode() for post in self.posts],
            "comments": [comment.encode() for comment in self.comments],
            "messages": [message.encode() for message in self.messages],
            "bio": self.bio
        }
