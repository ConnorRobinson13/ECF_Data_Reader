class Element:
    """
    A class representing an element in a category in an Excel sheet.

    Attributes:
        __name (str): The name of the element.
        __occurrences (int): The number of times the element appears in the category.
    """
    __name = None
    __occurrences = None

    def __init__(self, name, occurrences):
        """
        Construct a new `Element` object.

        Args:
            name (str): The name of the element.
            occurrences (int): The number of times the element appears in the category.

        Raises:
            ValueError: If `name` is None or has a length of 0.
            ValueError: If `occurrences` is less than 1.
        """
        self.set_name(name)
        self.set_occurrences(occurrences)

    def set_name(self, name):
        """
        Set the name of the element.

        Args:
            name (str): The name to set.

        Raises:
            ValueError: If `name` is None or has a length of 0.
        """
        if name is None or len(name) == 0:
            raise ValueError("Invalid Element Name")
        self.__name = name

    def get_name(self):
        """
        Get the name of the element.

        Returns:
            str: The name of the element.
        """
        return self.__name

    def set_occurrences(self, num):
        """
        Set the number of occurrences of the element.

        Args:
            num (int): The number to set.

        Raises:
            ValueError: If `num` is less than 1.
        """
        if num < 1:
            raise ValueError("Invalid Number of Occurrences")
        self.__occurrences = num

    def get_occurrences(self):
        """
        Get the number of occurrences of the element.

        Returns:
            int: The number of occurrences.
        """
        return self.__occurrences

    def to_string(self):
        return "Element Name: " + self.get_name() + ", Occurrences: " + str(self.get_occurrences())
