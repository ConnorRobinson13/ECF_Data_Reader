class Sheet:
    __sheet_name = None
    __categories = None

    def __init__(self, name):
        """
        Constructor for Sheet Object
        :param name: The name of this sheet
        """
        self.set_sheet_name(name)
        self.__categories = []

    def set_sheet_name(self, name):
        """
        Sets the name of the sheet
        :param name: The name to set
        :raise ValueError if name is None or the length of the name is 0
        """
        if name is None or len(name) == 0:
            raise ValueError("Invalid Sheet Name")
        self.__sheet_name = name

    def get_sheet_name(self):
        """
        Gets the name of the sheet
        :return: the name of the sheet
        """
        return self.__sheet_name

    def add_category(self, category):
        """
        Adds a category object to this sheet
        :param category: The category to add
        """
        self.__categories.append(category)

    def get_list_of_categories(self):
        """
        Gets a list of all the categories in the sheet
        :return: A list of all the categories in the sheet
        """
        return self.__categories

    def get_category(self, name):
        """
        Gets a specific category from the sheet by its name
        :param name: The name to search for and get
        :return: The category matching the name
        :raise ValueError if the name is not a category
        """
        for i in range(len(self.__categories)):
            if self.__categories[i].get_name() == name:
                return self.__categories[i]

        raise ValueError("Category Name does not exist")
