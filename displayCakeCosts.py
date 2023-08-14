from math import pi
from initializeWorkbook import currency_style


def displayCakeCosts(wb, recipes):
    ws = wb.create_sheet("Cake Costs")

    columns = ["Diameter"]
    for recipe in recipes:
        columns.append(recipe["name"])

    ws.append(columns)

    # add column of diameter values
    row = 2
    column = "A"
    for diameter in range(6, 15, 2):
        ws[f"{column}{row}"] = diameter
        row += 1

    # calculates the cost of the 8" cake for each recipe
    row = 3
    for recipe in recipes:
        column = chr(ord(column) + 1)
        # sum the products of the 'price per unit' from "Ingredient Data" sheet (D2:D17) and {column}2:{column}17 from "Recipe" sheet
        ws[f"{column}{row}"] = f"=SUMPRODUCT('Ingredient Data'!$D$2:$D$17, 'Recipes'!${column}$2:${column}$17)"

    # calculates the cost of the other cakes for each recipe
    eight_inch_area = pi * (8 / 2) ** 2
    column = "A"
    for recipe in recipes:
        column = chr(ord(column) + 1)
        for row in range(2, 7):
            if row != 3:
                diameter = ws[f"A{row}"].value
                current_area = pi * (diameter / 2) ** 2
                cost_proportion = current_area / eight_inch_area
                ws[f"{column}{row}"] = f"={column}$3 * {cost_proportion}"

    for row in ws.iter_rows(min_row=2, max_row=6, min_col=2, max_col=4):
        for cell in row:
            cell.style = currency_style

        


    

