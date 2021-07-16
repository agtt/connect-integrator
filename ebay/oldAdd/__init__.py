import logging
import requests
import json
import azure.functions as func
# from helper import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    # payload = json.dumps({
    #     # "categoryId": "",
    #     "condition": "NEW",
    #     "format": "FIXED_PRICE",
    #     "pricingSummary": {
    #         "price": {
    #             "currency": "GBP",
    #             "value": "150"
    #         }
    #     },
    #     "product": {
    #         "aspects": [
    #             {
    #                 "name": "string",
    #                 "values": [
    #                     "string"
    #                 ]
    #             }
    #         ],
    #         "brand": "string",
    #         "description": "string",
    #         "epid": "string",
    #         "imageUrls": [
    #             "https://cdn.pixabay.com/photo/2013/07/12/17/47/test-pattern-152459_960_720.png"
    #         ],
    #         "title": "string"
    #     }
    # })
    # response = callApi(url=EBAY_API['item_draft'], payload=payload)
    # response = json.dumps(response)

    return func.HttpResponse(
        f"test",
        status_code=200
    )
