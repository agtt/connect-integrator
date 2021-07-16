import json

import azure.functions as func
from helper import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    response = api().execute("GetSellerList", dict(
        ErrorLanguage='en_GB',
        WarningLevel='High',
        GranularityLevel='Coarse',
        StartTimeFrom='2021-07-10T21:59:59.005Z',
        StartTimeTo='2021-07-20T21:59:59.005Z',
        IncludeWatchCount=True,
        Pagination=dict(
            EntriesPerPage=30
        )
    ))
    items = response.dict()
    items = json.dumps(items)
    return func.HttpResponse(
        f"{items}",
        status_code=200
    )
