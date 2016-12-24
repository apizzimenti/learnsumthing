from pyramid.response import Response
from pyramid.view import view_config
from server.relationships import Container
from server.relationships import validate_results
from bson.objectid import ObjectId
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
            body=dumps(c.__dict__)
        )

    @view_config(route_name="student_GET")
    def student_GET(self):

        db = self.request.db.test
        name = self.request.params.get("name", None)
        objectId = self.request.params.get("_id", None)
        body = None

        if not name and not objectId:
            students = db.sumthing.find({"school.students": {}})
        elif name and not objectId:
            db.sumthing.find({"school.students.name": name})
        else:
            db.sumthing.find({"school.students._id": objectId})

        return Response(
            content_type="application/json",
            body=body
        )

    @view_config(route_name="school_GET")
    def school_GET(self):

        db = self.request.db.test
        name = self.request.params.get("name", None)
        location = self.request.params.get("location", None)
        objectId = self.request.params.get("_id", None)

        if objectId:
            result = db.sumthing.find_one({"_id": ObjectId(objectId)})
            result["_id"] = str(result["_id"])

            re = Container(data=[result])

            return Response(
                content_type="application/json",
                body=dumps(re.encode())
            )

        elif name and not location:
            result = db.sumthing.find({"name": name})
        elif name and location:
            result = db.sumthing.find({"name": name, "location": location})
        else:
            result = db.sumthing.find({"location": location})

        re = Container(data=validate_results(result))

        return Response(
            content_type="application/json",
            body=dumps(re.encode())
        )

    @view_config(route_name="school_POST")
    def school_POST(self):

        db = self.request.db.test
        req = self.request.json_body
        db.sumthing.insert_one(req)

        return Response(
            content_type="application/json",
            body=self.request.body
        )

