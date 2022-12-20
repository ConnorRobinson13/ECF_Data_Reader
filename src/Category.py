from src import Element


class Category:
    __categoryName = None
    __elements = None
    __data = None

    def __init__(self, name, data):
        """
        Default Constructor for Category Object will set the value fields correctly and then construct
         a list of elements based off the given list of data
        :param name: The name of the Category to set
        :param data: The List of Data to set
        """
        self.set_name(name)
        self.__elements = []
        self.__data = data

        self.__make_elements_list()

    def set_name(self, name):
        """
        Sets the name of the Category Object
        :param name: The name to set
        :raises ValueError if name is None or has a length of 0
        """
        if name is None or len(name) == 0:
            raise ValueError("Invalid Category Name")
        self.__categoryName = name

    def get_name(self):
        """
        Gets the name of this category
        :return: The name of the Category
        """
        return self.__categoryName

    def find_unique_elements(self):
        """
        Searches the list of data and returns a list of only the unique elements of data
        Ex. if [a,b,c,d,a] were passed [a,b,c,d] would be returned
        :return: A list of only the unique elements in the passed data list
        """
        unique_list = []
        for i in self.__data:
            if i not in unique_list:
                unique_list.append(i)
            else:
                pass

        return unique_list

    def add_data(self, element):
        """
        Adds data to the end of the list of elements, is used by make_element_list to create
        the __element field
        :param element: The Element object to add
        """
        self.__elements.append(element)

    def get_data(self):
        """
        Gets the data list
        :return: A list of the data field
        """
        return self.__data

    def get_elements(self):
        """
        Gets the list of elements in the category
        :return: The list of elements in this category
        """
        return self.__elements

    def __make_elements_list(self):
        """
        Checks to see how many times each unique element occurs in the data passed then makes an
        Element object with the information
        Used to create the Category object
        """
        unique = self.find_unique_elements()

        for i in range(len(unique)):
            temp_element = Element.Element(unique[i], self.__data.count(unique[i]))
            self.__elements.append(temp_element)
