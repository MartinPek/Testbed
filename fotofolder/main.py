# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from datetime import datetime as dt


def main():
    now = dt.now()
    folder_name = now.strftime("%Y_%m_%d")
    os.chdir("C:/Users/Kasse/KundenfotosST")
    os.mkdir(folder_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

