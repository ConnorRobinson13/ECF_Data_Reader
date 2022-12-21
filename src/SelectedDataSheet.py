from src.Sheet import Sheet


class SelectedDataSheet(Sheet):
    __categories = None
    __sheet_name = None

    def __init__(self):
        """
        Constructor for SelectedDataSheet that makes a sheet object and automatically sets the name
        to "Selected Categories"
        """
        super().__init__("Selected Categories")
