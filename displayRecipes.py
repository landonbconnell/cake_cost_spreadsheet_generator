def displayRecipes(wb, ingredients, recipes):
    ws = wb.create_sheet("Recipes")

    columns = ["Ingredient"]
    for recipe in recipes:
        columns.append(recipe["name"])

    ws.append(columns)

    row = 2
    column = "A"
    for ingredient in ingredients:
        ws[f"{column}{row}"] = ingredient["name"]
        row += 1

    for recipe in recipes:
        row = 2
        column = chr(ord(column) + 1)
        for ingredient in ingredients:
            matching_ingredient = None
            for recipe_ingredient in recipe["ingredients"]:
                if recipe_ingredient["name"] == ingredient["name"]:
                    matching_ingredient = recipe_ingredient
                    break
            # The recipe contains the ingredient, so add its quantity to the spreadsheet
            ws[f"{column}{row}"] = matching_ingredient["quantity"]["amount"] if matching_ingredient else 0
            row += 1
        
