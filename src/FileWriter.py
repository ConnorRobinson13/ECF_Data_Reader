def write_file(sheet):
    """
    Write the contents of the given sheet to a text file.

    The name of the text file will be the name of the sheet, with a '.txt' extension.

    Args:
        sheet: The sheet object to write to the text file.

    Returns:
        None
    """
    name = sheet.get_sheet_name() + ".txt"
    with open(name, "w") as file:
        file.write(sheet.to_string())
