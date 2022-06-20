import re

number = input("введите номер машины: ")


class ValidCarNumber:

    def __init__(self):
        self.number = number

    def is_valid(self, number):
        print(f"Number: {self.number}")


is_valid = re.search(r"(0)[1-9](KG)([0-9]{3})([A-Z]{3})", number)
try:
    if is_valid.end() == len(number):
        print("Car number is Valid!")
    else:
        raise ValueError
except:
    print("Car number invalid!")
