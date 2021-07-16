import azure.functions as func
from helper import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req = req.get_json()
        item = dict(
            Item=dict(
                Title=req.get('title', ''),
                Country=req.get('country', 'GB'),
                Location=req.get('location', 'GB'),
                Site=req.get('site', 'UK'),
                ConditionID="1000",
                PaymentMethods="VisaMC",
                # PaymentMethods="PayPal",
                PayPalEmailAddress="info@iova.co.uk",
                PrimaryCategory={"CategoryID": "20744"},
                Description=req.get('description', ''),
                ListingDuration=req.get('listing', 'Days_10'),
                ListingType=req.get('listing_type', 'FixedPriceItem'),
                StartPrice=req.get('price', ''),
                Currency=req.get('currency', 'USD'),
                DispatchTimeMax=req.get('dispatch', 3),
                PictureDetails=dict(
                    PictureURL='https://upload.wikimedia.org/wikipedia/en/thumb/3/39/Fenerbah%C3%A7e.svg/1200px-Fenerbah%C3%A7e.svg.png'
                ),
                ProductListingDetails=dict(
                    EAN=req.get('ean', ''),
                    # EAN="8054241786423",
                    UPC=req.get('upc', ''),
                    IncludeeBayProductDetails=True,
                    BrandMPN=dict(
                        Brand='Unbranded',
                        MPN='Unbranded_DSADA'
                    )
                ),
                ItemSpecifics=dict(
                    NameValueList=
                    [
                        dict(Name="manufacturer", Value="Unbranded")
                    ]

                ),
                ReturnPolicy=dict(
                    ReturnsAcceptedOption="ReturnsAccepted",
                    RefundOption="MoneyBack",
                    ReturnsWithinOption="Days_30",
                    # "Description": "If you are not satisfied, return the keyboard.",
                    ShippingCostPaidByOption="Buyer"
                ),
                ShippingDetails=dict(
                    ShippingServiceOptions=dict(
                        FreeShipping=req.get('free_shipping', True),
                        ShippingService="USPSParcel",
                        # ShippingService= "UK_RoyalMailSpecialDeliveryNextDay",
                        # ShippingServiceCost=""
                    )
                ),

            )
        )

        response = api().execute("AddItem", item)
        print(response.reply)
    except Exception as e:
        print(str(e))
        print('HATAAAA')

    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )
