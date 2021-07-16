import logging

import azure.functions as func
import time
import openapi_client
from pprint import pprint
from openapi_client.api import inventory_item_api
from openapi_client.model.availability import Availability
from openapi_client.model.availability_distribution import AvailabilityDistribution
from openapi_client.model.base_response import BaseResponse
from openapi_client.model.bulk_get_inventory_item import BulkGetInventoryItem
from openapi_client.model.bulk_get_inventory_item_response import BulkGetInventoryItemResponse
from openapi_client.model.bulk_inventory_item import BulkInventoryItem
from openapi_client.model.bulk_inventory_item_response import BulkInventoryItemResponse
from openapi_client.model.bulk_price_quantity import BulkPriceQuantity
from openapi_client.model.bulk_price_quantity_response import BulkPriceQuantityResponse
from openapi_client.model.dimension import Dimension
from openapi_client.model.inventory_item import InventoryItem
from openapi_client.model.inventory_item_with_sku_locale import InventoryItemWithSkuLocale
from openapi_client.model.inventory_item_with_sku_locale_groupid import InventoryItemWithSkuLocaleGroupid
from openapi_client.model.inventory_items import InventoryItems
from openapi_client.model.package_weight_and_size import PackageWeightAndSize
from openapi_client.model.pickup_at_location_availability import PickupAtLocationAvailability
from openapi_client.model.product import Product
from openapi_client.model.ship_to_location_availability import ShipToLocationAvailability
from openapi_client.model.time_duration import TimeDuration
from openapi_client.model.weight import Weight

configuration = openapi_client.Configuration(
    host = "https://api.sandbox.ebay.com/sell/inventory/v1"
    # host = "https://api.ebay.com/sell/inventory/v1"
)
configuration.access_token = 'v^1.1#i^1#p^3#r^0#f^0#I^3#t^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'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = inventory_item_api.InventoryItemApi(api_client)
        bulk_inventory_item = BulkInventoryItem(
            requests=[
                InventoryItemWithSkuLocale(
                    availability=Availability(
                        # pickup_at_location_availability=[
                        #     PickupAtLocationAvailability(
                        #         availability_type="availability_type_example",
                        #         fulfillment_time=TimeDuration(
                        #             unit="unit_example",
                        #             value=1,
                        #         ),
                        #         merchant_location_key="merchant_location_key_example",
                        #         quantity=1,
                        #     ),
                        # ],
                        ship_to_location_availability=ShipToLocationAvailability(
                            # availability_distributions=[
                            #     AvailabilityDistribution(
                            #         fulfillment_time=TimeDuration(
                            #             unit="unit_example",
                            #             value=1,
                            #         ),
                            #         merchant_location_key="merchant_location_key_example",
                            #         quantity=1,
                            #     ),
                            # ],
                            quantity=1,
                        ),
                    ),
                    condition="NEW",
                    condition_description="condition_description_example",
                    # locale="en_US",
                    locale="en_GB",
                    # package_weight_and_size=PackageWeightAndSize(
                    #     # dimensions=Dimension(
                    #     #     height=3.14,
                    #     #     length=3.14,
                    #     #     unit="unit_example",
                    #     #     width=3.14,
                    #     # ),
                    #     package_type="",
                    #     # weight=Weight(
                    #     #     unit="unit_example",
                    #     #     value=3.14,
                    #     # ),
                    # ),
                    product=Product(
                        # aspects=[
                        # ],
                        price=10,
                        brand="markasi",
                        description="aciklaamar deneme",
                        # ean=[
                        #     "8698806201329",
                        # ],
                        epid="",
                        image_urls=[
                            "https://cdn.pixabay.com/photo/2013/07/12/17/47/test-pattern-152459_960_720.png",
                        ],
                        # isbn=[
                        #     "isbn_example",
                        # ],
                        mpn="8698806201329",
                        subtitle="altbaslik",
                        title="lan bu bir urun",
                        # upc=[
                        #     "",
                        # ],
                    ),
                    sku="8698806201331",
                ),
            ],
        )  # BulkInventoryItem | Details of the inventories with sku and locale

        try:
            api_response = api_instance.bulk_create_or_replace_inventory_item(bulk_inventory_item)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling InventoryItemApi->bulk_create_or_replace_inventory_item: %s\n" % e)

    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )