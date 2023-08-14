# Cake Cost Spreadsheet Generator
# This script will generate a spreadsheet of cake costs based on the current cost of ingredients and the recipe for each cake.
# This task will be accomplished via the Kroger API and OpenPyXL.

import asyncio
from openpyxl import Workbook
from getAccessToken import *
from getLocation import *
from getIngredientPrice import *
from ingredients import *

# wb = Workbook()
# ws = wb.active

# ws.title = "Current Ingredient Costs"

async def main():
    # gets the access token for the Kroger API
    print('Getting access token... ', end='', flush=True)
    access_token = getAccessToken()
    print('done')
    
    # gets the location of the nearest Kroger store, replace zip code with your own
    print('Getting closest Kroger location... ', end='', flush=True)
    zip_code = '43062'
    location = getLocation(access_token, zip_code)
    location_id = location["locationId"]
    print('done')

    print('Getting ingredient prices... ', end='', flush=True)
    for ingredient in ingredients:
        price = getIngredientPrice(access_token, location_id, ingredient["id"])
        ingredient["price"] = str(price)
    print('done')

if __name__ == "__main__":
    asyncio.run(main())
