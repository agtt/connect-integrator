import logging

import azure.functions as func
# import json
# import openapi_client
# from pprint import pprint
# from openapi_client.api import inventory_item_api
# from openapi_client.model.availability import Availability
# from openapi_client.model.availability_distribution import AvailabilityDistribution
# from openapi_client.model.base_response import BaseResponse
# from openapi_client.model.bulk_get_inventory_item import BulkGetInventoryItem
# from openapi_client.model.bulk_get_inventory_item_response import BulkGetInventoryItemResponse
# from openapi_client.model.bulk_inventory_item import BulkInventoryItem
# from openapi_client.model.bulk_inventory_item_response import BulkInventoryItemResponse
# from openapi_client.model.bulk_price_quantity import BulkPriceQuantity
# from openapi_client.model.bulk_price_quantity_response import BulkPriceQuantityResponse
# from openapi_client.model.dimension import Dimension
# from openapi_client.model.inventory_item import InventoryItem
# from openapi_client.model.inventory_item_with_sku_locale import InventoryItemWithSkuLocale
# from openapi_client.model.inventory_item_with_sku_locale_groupid import InventoryItemWithSkuLocaleGroupid
# from openapi_client.model.inventory_items import InventoryItems
# from openapi_client.model.package_weight_and_size import PackageWeightAndSize
# from openapi_client.model.pickup_at_location_availability import PickupAtLocationAvailability
# from openapi_client.model.product import Product
# from openapi_client.model.ship_to_location_availability import ShipToLocationAvailability
# from openapi_client.model.time_duration import TimeDuration
# from openapi_client.model.weight import Weight

# configuration = openapi_client.Configuration(
#     host = "https://api.sandbox.ebay.com/sell/inventory/v1"
#     # host = "https://api.ebay.com/sell/inventory/v1"
# )
# configuration.access_token = 'v^1.1#i^1#p^3#r^0#f^0#I^3#t^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'


def main(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')
    # with openapi_client.ApiClient(configuration) as api_client:
    #     # Create an instance of the API class
    #     api_instance = inventory_item_api.InventoryItemApi(api_client)
    #     items = api_instance.get_inventory_items()
    return func.HttpResponse(
     f"f",
         status_code=200
    )
