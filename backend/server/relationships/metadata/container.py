from datetime import datetime


class Container:

    def __init__(self, data=None, errors=None):
        self.data = data
        self.errors = errors

        timestamp = datetime.now().time().strftime("%H:%M:%S")
        authors = [
            "Anthony Pizzimenti"
        ]
        copyright = "Anthony Pizzimenti 2016"

        self.metadata = {
            "timestamp": timestamp,
            "copyright": copyright,
            "authors": authors
        }