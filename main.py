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
    access_token = getAccessToken()
    zip_code = '43062'

    # gets the location of the nearest Kroger store
    location = getLocation(access_token, zip_code)
    location_id = location["locationId"]

    tasks = []
    for ingredient in ingredients:
        tasks.append(getIngredientPrice(access_token, location_id, ingredient["id"]))

    await asyncio.gather(*tasks)

    print(ingredients)

if __name__ == "__main__":
    asyncio.run(main())
