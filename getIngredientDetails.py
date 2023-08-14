import requests
from convertToOunces import *

# returns the price and size of a specific ingredient
def getIngredientDetails(access_token, location_id, product_id):
    url = f"https://api.kroger.com/v1/products/{product_id}?filter.locationId={location_id}"

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            # get the cheapest price for the current ingredient
            product_details = data["data"]["items"][0]

            prices = product_details["price"]
            if prices["promo"] != 0:
                price = prices["promo"]
            else:
                price = prices["regular"]

            size = product_details["size"]
            size = convertToOunces(size) # converts the size to ounces

            return {
                "price": price,
                "size": size
            }

        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None
