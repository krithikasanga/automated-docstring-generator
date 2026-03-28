# test_optimization.py

def find_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def calculate_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def check_user(username, password):
    if username == "admin" and password == "1234":
        return True
    return False


def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result


def format_phone(number):
    number = str(number)
    part1 = number[:3]
    part2 = number[3:6]
    part3 = number[6:]
    return "(" + part1 + ") " + part2 + "-" + part3


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def count(self):
        return len(self.items)

    def clear(self):
        self.items = []