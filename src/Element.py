class Element:
    __name = None
    __occurrences = None

    def __init__(self, name, occurrences):
        """
        Default constructor for Element object
        :param name: The name to set the element name to
        :param occurrences: The amount of times the element occurs in a specific category
        """
        self.set_name(name)
        self.set_occurrences(occurrences)

    def set_name(self, name):
        """
        Sets the name of the element
        :param name: The name to set
        :raises ValueError if the name is empty or None
        """
        if name is None or len(name) == 0:
            raise ValueError("Invalid Element Name")
        self.__name = name

    def get_name(self):
        """
        Gets the name of this element
        :return: The name of the element
        """
        return self.__name

    def set_occurrences(self, num):
        """
        Sets the number of times an element appears in a category
        :param num: The number to set
        :raises ValueError if the number is less than 1
        """
        if num < 1:
            raise ValueError("Invalid Number of Occurrences")
        self.__occurrences = num

    def get_occurrences(self):
        """
        Gets the number of times an element appears in a category
        :return: The number of occurrences
        """
        return self.__occurrences
