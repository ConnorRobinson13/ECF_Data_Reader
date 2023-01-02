import sys
import os

from src.FileReader import *
from src.FileWriter import write_file


def main():
    # Print a prompt to the console
    print("Please enter a file path of an Excel Sheet:")

    # Read the file path from the user input
    file_path = input()

    sheet = read_excel_file(file_path)

    def clear_console():
        # If the operating system is Windows, use the cls command
        if os.name == "nt":
            os.system("cls")
        # If the operating system is Linux, macOS, or Unix, use the clear command
        else:
            os.system("clear")

    # Call the clear_console function to clear the console
    clear_console()

    print("Here is the Digested Data from your Excel Sheet broken into categories:\n\n")
    print(sheet.to_string())


if __name__ == "__main__":
    main()
