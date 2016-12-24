from .things import *
from .metadata import *
from .people import *
from .interactions import *


# function to serialize ObjectIds
def validate_results(results):

    data = []

    for result in results:
        result["_id"] = str(result["_id"])
        data.append(result)

    return data
