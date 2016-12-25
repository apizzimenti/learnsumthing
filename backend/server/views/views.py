from pyramid.response import Response
from pyramid.view import view_config
from server.relationships import Container
from json import loads, dumps


class Server:

    def __init__(self, request):
        self.request = request

    @view_config(route_name="home")
    def home(self):

        message = ["Welcome to the learnsumthing api base page. For more info, visit the\
        documentation at {0} for more information.".format("")]

        c = Container(message)

        return Response(
            content_type="application/json",
            body=dumps(c.encode())
        )
