class Sheet:
    __sheet_name = None
    __categories = None

    def __init__(self, name):
        self.set_sheet_name(name)
        self.__categories = []

    def set_sheet_name(self, name):
        if name is None or len(name) == 0:
            raise ValueError("Invalid Sheet Name")
        self.__sheet_name = name

    def get_sheet_name(self):
        return self.__sheet_name

    def add_category(self, category):
        self.__categories.append(category)

    def get_list_of_categories(self):
        return self.__categories

    def get_category(self, name):
        for i in range(len(self.__categories)):
            if self.__categories[i].get_name() == name:
                return self.__categories[i]

        raise ValueError("Category Name does not exist")
