import logging
import azure.functions as func
from helper import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', None)
    if name is None:
        return func.HttpResponse(
            "Please provide a name",
            status_code=400
        )

    response = api().execute('GetSuggestedCategories', {'Query': name})

    return func.HttpResponse(
        f"{response.json()}",
        status_code=200
    )
