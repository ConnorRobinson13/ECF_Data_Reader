from src.FileReader import *
from src.FileWriter import write_file
from src.Sheet import Sheet


class SheetManager:
    __currentSheet = None
    __selectedDataSheet = None

    def __init__(self):
        self.__selectedDataSheet = Sheet("Selected Data")

    def set_current_sheet(self, sheet):
        self.__currentSheet = sheet

    def get_current_sheet(self):
        if self.__currentSheet is None:
            raise ValueError("No Sheet has been loaded")
        else:
            return self.__currentSheet

    def get_category(self, category):
        if self.__currentSheet is None:
            raise ValueError("No Sheet has been loaded")

        categories = self.__currentSheet.get_categories()
        for i in range(len(categories)):
            if categories[i].get_name() == category.get_name():
                return categories[i]

        raise ValueError("Category does not exist in the current sheet")

    def get_categories(self):
        if self.__currentSheet is None:
            raise ValueError("No Sheet has been loaded")
        return self.__currentSheet.get_categories()

    def get_selected_sheet(self):
        if self.__currentSheet is None:
            raise ValueError("No Sheet has been loaded")
        return self.__selectedDataSheet

    def add_to_selected(self, category):
        if self.__currentSheet is None:
            raise ValueError("No Sheet has been loaded")
        self.__selectedDataSheet.add_category(category)

    def remove_from_selected(self, category):
        if self.__currentSheet is None:
            raise ValueError("No Sheet has been loaded")
        if len(self.__selectedDataSheet.get_categories()) == 0:
            raise ValueError("No Categories have been selected")
        self.__selectedDataSheet.remove(category)

    def load_sheet(self, file_name):
        sheet = read_excel_file(file_name)
        self.set_current_sheet(sheet)

    def save_data_full(self):
        write_file(self.__currentSheet)

    def save_data_selected(self):
        write_file(self.__selectedDataSheet)