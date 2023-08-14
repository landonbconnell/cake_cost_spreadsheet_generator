# Cake Cost Spreadsheet Generator
# This script will generate a spreadsheet of cake costs based on the current cost of ingredients and the recipe for each cake.
# This task will be accomplished via the Kroger API and OpenPyXL.

from openpyxl import Workbook
from getAccessToken import *
from getLocation import *
from getIngredientDetails import *
from ingredients import *
from initializeWorkbook import *
from displayIngredientData import *
from displayRecipes import *
from recipes import *

def main():

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

    # gets the current price and size of each ingredient
    print('Getting ingredient prices... ', end='', flush=True)
    for ingredient in ingredients:
        if ingredient["id"]:
            data = getIngredientDetails(access_token, location_id, ingredient["id"])
            price, size = data["price"], data["size"]
            ingredient["price"] = price
            ingredient["size"] = size
    print('done')

    # initializes the workbook
    print('Initializing Workbook... ', end='', flush=True)
    wb = initializeWorkbook()
    print('done')

    # writes the ingredient data to a spreadsheet
    print('Writing ingredient data to a spreadsheet... ', end='', flush=True)
    displayIngredientData(wb, ingredients)
    print('done')

    # writes the recipes to a spreadsheet
    print('Writing recipes to a spreadsheet... ', end='', flush=True)
    displayRecipes(wb, ingredients, recipes)
    print('done')

    wb.save("cake_costs.xlsx")

if __name__ == "__main__":
    main()
