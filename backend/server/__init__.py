from pyramid.config import Configurator
from pymongo import MongoClient
from urllib.parse import urlparse


def main(global_config, **settings):
    # config
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # database
    db_uri = urlparse(settings["mongo_uri"])
    config.registry.db = MongoClient(host=db_uri.hostname, port=db_uri.port)

    def add_db(request):
        return config.registry.db

    config.add_request_method(add_db, 'db', reify=True)

    # routes for API
    # index
    config.add_route("home", '/')
    # student
    config.add_route("student_GET", "/student", request_method="GET")
    config.add_route("student_POST", "/student", request_method="POST")
    config.add_route("school_GET", "/school", request_method="GET")
    config.add_route("school_POST", "/school", request_method="POST")
    config.scan(".views")

    return config.make_wsgi_app()
