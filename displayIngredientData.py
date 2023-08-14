def displayIngredientData(wb, ingredients):
    ws = wb.active
    ws.title = "Ingredient Data"
    data = [["Ingredient", "Price", "Size (oz)", "Price Per Unit"]]

    for ingredient in ingredients:
        price_per_unit = float(ingredient["price"]) / float(ingredient["size"])
        data.append([ingredient["name"], ingredient["price"], ingredient["size"], price_per_unit])

    for row in data:
        ws.append(row)
    
    # Set the currency format for the "price" and "price per unit" columns
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=2, max_col=2):  # adjusting for "price" column
        for cell in row:
            cell.style = "currency_style"
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=4, max_col=4):  # adjusting for "price per unit" column
        for cell in row:
            cell.style = "currency_style"
    
    
