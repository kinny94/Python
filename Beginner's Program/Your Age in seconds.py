__author__ = "arjun"


def ask_age():
    age = input("Enter your age: ")
    return int(age)


def calculate_seconds(age):
    return age * 365 * 60 * 60


def prompt():
    age = ask_age()
    seconds = calculate_seconds(age)
    print ("Your age in seconds is : {}".format(seconds))


prompt()
