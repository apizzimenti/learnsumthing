from datetime import datetime


class Message:

    def __init__(self, author, recipient, body="", read=False):
        self.body = body
        self.author = author
        self.recipient = recipient
        self.read = read

        self.timestamp = datetime.now().time().strftime("%H:%M:%S")

    def encode(self):

        return {
            "body": self.body,
            "author": self.author.encode(),
            "recipient": self.recipient.encode(),
            "read": self.read
        }