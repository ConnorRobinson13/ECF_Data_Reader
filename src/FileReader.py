import xlrd

from src.Category import Category
from src.Sheet import Sheet


def read_excel_file(file):
    """
    Read an Excel file and return a Sheet object containing the data from the first sheet in the file.

    Args:
        file (str): The path to the Excel file.

    Returns:
        Sheet: A Sheet object containing the data from the first sheet in the Excel file.
    """
    # Open the workbook
    workbook = xlrd.open_workbook(file)

    # Get the first sheet
    page = workbook.sheet_by_index(0)

    # Process the sheet and return a Sheet object
    return process_sheet(page)


def process_sheet(page):
    """
    Process a sheet from an Excel workbook and return a Sheet object containing the data from the sheet.

    Args:
        page (xlrd.sheet.Sheet): The sheet to be processed.

    Returns:
        Sheet: A Sheet object containing the data from the sheet.
    """
    # Create a new Sheet object with the name of the sheet
    sheet = Sheet(page.name)

    # Process each column in the sheet and add a Category object to the Sheet object
    for i in range(0, len(page.row_values(0))):
        sheet.add_category(process_category(page, i))

    return sheet


def process_category(page, col):
    """
    Process a column in a sheet from an Excel workbook and return a Category object containing the data from the column.

    Args:
        page (xlrd.sheet.Sheet): The sheet containing the column.
        col (int): The index of the column to be processed.

    Returns:
        Category: A Category object containing the data from the column.
    """
    data = []
    # Get the name of the category from the first row in the column
    name = page.col_values(col)[0]

    # Process each cell in the column
    for i in range(1, len(page.col_values(col))):
        app = page.cell_value(i, col)

        # If the cell contains a boolean value, convert it to a string
        if page.cell(i, col).ctype == xlrd.XL_CELL_BOOLEAN:
            if page.cell_value(i, col) == 1:
                app = "True"
            else:
                app = "False"

        # If the cell contains a date, convert it to a string
        if page.cell(i, col).ctype == xlrd.XL_CELL_DATE:
            date_val = xlrd.xldate_as_datetime(page.cell(i, col).value, 0)
            app = date_val.strftime('%m/%d/%Y')

        # Add the cell value to the data list
        data.append(app)

    # Create a new Category object with the name and data
    category = Category(name, data)

    return category



