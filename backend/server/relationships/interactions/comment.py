

class Comment:

    def __init__(self, post, body="", parent=None, child=None):
        self.body = body
        self.post = post
        self.parent = parent
        self.child = child

    def encode(self):

        d = {
            "body": self.body
        }

        if self.parent:
            d["parent"] = self.parent.encode()

        if self.child:
            d["child"] = self.parent.encode()

        return d
