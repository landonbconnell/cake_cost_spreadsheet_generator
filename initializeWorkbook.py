from openpyxl import Workbook
from openpyxl.styles import NamedStyle

def initializeWorkbook():
    wb = Workbook()

    # Define the currency style
    currency_style = NamedStyle(name="currency_style", number_format="$0.00")

    # Add named style to the workbook if it doesn't exist
    if "currency_style" not in wb.named_styles:
        wb.add_named_style(currency_style)
    
    return wb