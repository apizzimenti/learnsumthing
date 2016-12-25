from pyramid.response import Response
from pyramid.view import view_config
from server.relationships import Container
from server.relationships import validate_results
from bson.objectid import ObjectId
from json import loads, dumps


class StudentViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name="student_GET")
    def student_GET(self):

        db = self.request.db.test
        name = self.request.params.get("name", None)
        objectId = self.request.params.get("_id", None)

        if objectId:
            result = db.sumthing.find_one({"students._id": objectId})
            result["_id"] = str(result["_id"])

            re = Container(data=result)

            return Response(
                content_type="application/json",
                body=dumps(re.encode())
            )

        elif not name and not objectId:
            result = db.sumthing.find({"students": {}})
        elif name and not objectId:
            result = db.sumthing.find({"students.name": name})

        re = Container(data=validate_results(result))

        return Response(
            content_type="application/json",
            body=dumps(re.encode())
        )

    @view_config(route_name="student_POST")
    def student_POST(self):

        db = self.request.db.test
        req = self.request.json_body
        students = db.sumthing.find_one({"_id": ObjectId(req["school_id"])})
        print(students)

        db.sumthing.update_one(
            {"_id": ObjectId(req["school_id"])},
            {"$set": {"students": students.append(req)}}
        )

        return Response(
            content_type="application/json",
            body=req
        )